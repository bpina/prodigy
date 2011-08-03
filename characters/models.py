from django.db import models
from django.contrib.auth.models import User
from guilds.models import Guild
from servers.models import Server

class Character(models.Model):
  name = models.CharField(max_length=255)
  server = models.ForeignKey(Server)
  guild = models.ForeignKey(Guild, blank=True,null=True)
  user = models.ForeignKey(User)
  is_guild_master = models.BooleanField()
  is_default = models.BooleanField()

  def __str__(self):
    return self.name
