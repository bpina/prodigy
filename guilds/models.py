from django.db import models
from servers.models import Server
from django.contrib import auth

# Create your models here.
class Guild(models.Model):
  name = models.CharField(max_length=255)
  server = models.ForeignKey(Server)
  user = models.ForeignKey(auth.models.User)

  def get_guild_master(self):
    return self.character_set.filter(character__is_guild_master=True)

  def __str__(self):
    return self.name
