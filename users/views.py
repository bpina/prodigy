from django.shortcuts import render_to_response, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from characters.forms import CharacterForm

def index(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/security/login')
  characters = request.user.character_set.all()
  data = {'characters': characters}

  return render(request, 'users/index.html', data)
