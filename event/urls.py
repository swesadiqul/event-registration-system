from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'events'

#create urls here
urlpatterns = [
    path('', views.index, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('registrations/<int:event_id>/unregister/', views.unregister_from_event, name='unregister_from_event'),
    path('registered-events/', views.registered_events, name='registered_events'),


    #create api endpoint here
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/events/', views.EventList.as_view(), name='event-list'),
    path('api/events/<int:event_id>/', views.EventDetail.as_view(), name='event-detail'),
    path('api/user-events/<int:event_id>/', views.UserEventRegistration.as_view(), name='user-event-registration'),
    path('api/user-events/', views.UserRegisteredEvents.as_view(), name='user-registered-events'),
]
