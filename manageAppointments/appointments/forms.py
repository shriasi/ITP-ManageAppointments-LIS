from django import forms
from django.core import validators
from appointments.models import Appointments

#form to enter appointment
class AppointForm(forms.ModelForm):  
    class Meta:  
        model = Appointments  
        fields = "__all__"
