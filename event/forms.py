from django import forms
from .models import Event



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location_name', 'available_slots']


class RegistrationForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())
