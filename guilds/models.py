from django.db import models
from characters.models import Server

# Create your models here.
class Guild(models.Model):
  name = models.CharField(max_length=255)
  server = models.ForeignKey(Server)
