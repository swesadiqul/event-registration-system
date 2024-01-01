from django.urls import path
from . import views


app_name = 'events'

#create urls here
urlpatterns = [
    path('', views.index, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('registrations/<int:event_id>/unregister/', views.unregister_from_event, name='unregister_from_event'),
    path('registered-events/', views.registered_events, name='registered_events'),
]
