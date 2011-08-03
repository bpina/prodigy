# Create your views here.
from guilds.models import Guild
from guilds.forms import GuildForm
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

def show(request, server_name, guild_name):
  g = get_object_or_404(Guild,server__name=server_name,name=guild_name)
  characters = g.character_set.all()

  return render(request, 'guilds/show.html', {'characters': characters, 'guild': g})  

def create(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect('/register')

  character = request.user.character_set.get(is_default=True)
  if not character or character.is_guild_master or character.guild:
    return HttpResponseRedirect('/')

  if request.method == 'GET':
    guild_form = GuildForm()
    return render(request, 'guilds/new.html', {'form': guild_form, 'character': character})
  else:
    guild_form = GuildForm(request.POST)
    if guild_form.is_valid():
      guild = guild_form.save(commit=False)
      guild.server = character.server
      guild.user = request.user
      guild.save()
      
      character.guild = guild
      character.is_guild_master = True
      character.save()
      return HttpResponseRedirect('/guilds/' + guild.server.name + '/' + guild.name)
