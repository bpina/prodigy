from django import forms
from django.forms import ModelForm
from characters.models import Character
from servers.models import Server

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    fields = ('name','server')

class UpdateDefaultCharacterForm(ModelForm):
  is_default = forms.BooleanField(required=False,initial=False)
  
  class Meta:
    model = Character
    fields = ('is_default',)
