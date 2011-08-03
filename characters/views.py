from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from characters.models import Character, Server
from characters.forms import CharacterForm, UpdateDefaultCharacterForm
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from django.utils import simplejson
# Create your views here.

def index(request):
  c = Character.objects.all()
  return render(request, 'characters/index.html', {'characters': c})

def show(request, server_name, character_name):
  c = get_object_or_404(Character, name=character_name, server__name=server_name)
  return render(request, 'characters/show.html', {'character': c})

@csrf_protect
def create(request):
  if request.method == 'GET':
    return HttpResponse(status=404)
  else:
    form = CharacterForm(request.POST)
    if form.is_valid():
      c = form.save(commit=False)
      c.user = request.user
      c.save()
    
      data = serializers.serialize('json', [c])
      if request.is_ajax():
        return HttpResponse(data, "application/javascript")
      else:
        return HttpResponseRedirect('/users/' + c.user.username)
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
