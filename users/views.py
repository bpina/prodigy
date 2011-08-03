from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from characters.forms import CharacterForm

def show(request, username):
  displayed_user = User.objects.get(username=username)
  characters = displayed_user.character_set.all()
  data = {'displayed_user': displayed_user, 'characters': characters}

  if request.user.username == displayed_user.username:
    data['session_user'] = True
    data['create_character_form'] = CharacterForm()

  return render(request, 'users/show.html', data)
