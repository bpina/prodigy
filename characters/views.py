from django.shortcuts import render_to_response
from characters.models import Character

# Create your views here.

def index(self):
  c = Character.objects.all()
  return render_to_response('characters/index.html', {'characters': c})
