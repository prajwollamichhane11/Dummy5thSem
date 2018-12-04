from django.db import models
from django.utils import timezone


# Create your models here.
class Dummy(models.Model):
	name = models.CharField(max_length = 200)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
