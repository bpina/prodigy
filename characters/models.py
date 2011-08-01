from django.db import models

# Create your models here.
class Server(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name

class Character(models.Model):
  name = models.CharField(max_length=255)
  server = models.ForeignKey(Server)

  def __str__(self):
    return self.name
