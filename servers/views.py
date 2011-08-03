from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from servers.models import Server

def show(request, server_name):
  s = get_object_or_404(Server, name=server_name)
  characters = s.character_set.all()
  
  return render(request, 'servers/show.html', {'server': s, 'characters': characters})
