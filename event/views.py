from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from django.db.models import Q

#rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *



# Create your views here.
def index(request):
    query = request.GET.get('q')

    if query:
        events = Event.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location_name__icontains=query)
        )
    else:
        events = Event.objects.all()

    return render(request, 'index.html', {'events': events, 'query': query})


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def event_list(request):
    query = request.GET.get('q')

    if query:
        events = Event.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location_name__icontains=query)
        )
    else:
        events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events, 'query': query})


@login_required(login_url='accounts:login')
def register_for_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    user = request.user
    registration, created = Registration.objects.get_or_create(user=user, event=event)
    if not created:
        messages.warning(request, 'You are already registered for this event.')
    else:
        event.available_slots -= 1
        event.save()
        messages.success(request, 'Successfully registered for the event.')
    return redirect('events:event_list')


@login_required
def unregister_from_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    registration = Registration.objects.get(user=request.user, event=event)

    # Unregister the user from the event
    registration.delete()
    event.available_slots += 1
    event.save()
    messages.success(request, 'Successfully unregistered for the event.')
    return redirect('events:event_list')


@login_required(login_url='accounts:login')
def registered_events(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/registered_events.html', {'registrations': registrations})




#api views here

class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventDetail(APIView):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event)
        return Response(serializer.data)


class UserEventRegistration(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, event_id):
        user = request.user

        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Check if there are available slots
        if event.available_slots <= 0:
            return Response({'message': 'No available slots for registration.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already registered for the event
        if Registration.objects.filter(user=user, event=event).exists():
            return Response({'message': 'User is already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create registration
        registration = Registration(user=user, event=event)
        registration.save()

        # Decrement available slots
        event.available_slots -= 1
        event.save()

        # serializer = RegistrationSerializer(registration)
        return Response({'message': 'Your registration for the event was successful.'}, status=status.HTTP_201_CREATED)


class UserRegisteredEvents(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        user_events = Registration.objects.filter(user=user)
        serializer = RegistrationSerializer(user_events, many=True)
        return Response(serializer.data)


