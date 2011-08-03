from django import forms
from django.forms import ModelForm
from guilds.models import Guild

class GuildForm(ModelForm):
  class Meta:
    model = Guild
    fields = ('name',)
