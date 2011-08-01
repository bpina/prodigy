from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpRequest, HttpResponse
from characters.models import Character, Server
from characters.forms import CharacterForm
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
# Create your views here.

def index(request):
  c = Character.objects.all()
  return render_to_response( 'characters/index.html', {'characters': c})

def show(request, character_id):
  c = get_object_or_404(Character, pk=character_id)
  return render_to_response('characters/show.html', {'character': c})

@csrf_protect
def create(request):
  if request.method == 'GET':
    c = Character()
    form = CharacterForm(instance=c)
    return render(request, 'characters/new.html', {'form': form})
  else:
    if request.is_ajax() != True:
      return HttpResponse(status=400)

    form = CharacterForm(request.POST)
    if form.is_valid():
      c = form.save(commit=False)
      c.save()
    
      data = serializers.serialize('json', [c])
      return HttpResponse(data, "application/javascript")
    else:
      return HttpResponse(status=400)
      
