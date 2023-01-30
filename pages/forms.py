from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class ReservationForm(forms.ModelForm):
  class Meta:
    model=Reservation
    fields="__all__"
    
    
class CreateUser(UserCreationForm):
  class Meta:
    model=User
    fields=["username","email","password1","password2"]