from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EventForm, RegistrationForm



# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {"events": events})


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


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

