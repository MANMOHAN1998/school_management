from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ClassForm(forms.ModelForm):    
    class Meta:
        model = Class
        fields = ['class_name']

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
