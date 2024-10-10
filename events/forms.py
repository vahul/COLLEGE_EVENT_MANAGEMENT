from django import forms
from events.models import Us, UserEvent

class UserForm(forms.ModelForm):
    class Meta:
        model = Us
        fields = ['gender', 'age', 'branch', 'year', 'section', 'university']
        # Add other fields as needed

class UserEventForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields = ['event']

from .models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'lecturer_name']
