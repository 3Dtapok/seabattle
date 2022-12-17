from django.db import models
from django.contrib.auth.models import User

class Lobby(models.Model):
	lock = models.BooleanField("Занято")

	#def __str__(self):
    #    return self.lock