from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from characters.models import Character, Server
from characters.forms import CharacterForm, UpdateDefaultCharacterForm
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from django.utils import simplejson
from pyarmory import assets
from mongoarmory.tools import get_character_info, get_appropriate_raids
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
  c = Character.objects.all()
  return render(request, 'characters/index.html', {'characters': c})

def show(request, server_name, character_name):
  c = get_object_or_404(Character, name=character_name, server__name=server_name)
  character_info = get_character_info(server_name, character_name)
  raids = get_appropriate_raids(character_info)

  return render(request, 'characters/show.html', {'character': c, 'character_data': character_info, 'raids': raids})

@csrf_protect
def create(request):
  if request.method == 'GET':
    return render(request, 'characters/new.html', {'form': CharacterForm()})
  else:
    form = CharacterForm(request.POST)
    if form.is_valid():
      c = form.save(commit=False)
      c.user = request.user

      if

      c.save()
    
      data = serializers.serialize('json', [c])
      if request.is_ajax():
        return HttpResponse(data, "application/javascript")
      else:
        return HttpResponseRedirect('/characters/' + str(c.server) + str(c))
    else:
      return HttpResponse(status=400)

def update(request):
  if request.method == 'GET':
    return HttpResponse(status=404)

  if request.POST:
    character_id = request.POST['id']
    c = Character.objects.get(pk=character_id)
    form = UpdateDefaultCharacterForm(request.POST, instance=c)
    if form.is_valid():
      c = form.save()
      c.save()
      if request.is_ajax():
        return HttpResponse(simplejson.dumps({'success': True, 'is_default': c.is_default, 'character_id': c.id}), "application/json")     
      else:
        return HttpResponseRedirect('/characters/' + c.server + '/' + c.name)
    else:
      if request.is_ajax():
        errors = {'errors': form.errors}
        return HttpResponse(simplejson.dumps(errors), "application/json")
      else:
        return HttpResponseRedirect('/characters/update')
  else:
    return HttpResponse(status=400)

def current(request):
  user = request.user
  if request.method == 'GET':
    if not user.character_set.all():
      return HttpResponseRedirect('/characters/create')
    characters = user.character_set.filter(is_default=False)
    return render(request, 'characters/current.html', {'characters': characters})
  else:
    if request.POST:
      pk = request.POST['character']
      c = user.character_set.get(pk=pk)
      old = user.character_set.filter(is_default=True)
      if old:
        old[0].is_default = False
        old[0].save()
      c.is_default = True
      c.save()
      return HttpResponseRedirect('/user/')
    else:
      return HttpResponse(status=500)
      
      
        
      
