from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
  username = forms.CharField()
  password_one = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')
  password_two = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirm Password')
  
  class Meta:
    model = User
    fields = ('username', 'email')
  
