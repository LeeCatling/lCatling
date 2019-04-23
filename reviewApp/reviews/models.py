from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Issue(models.Model):
	type=models.CharField(max_length=100)
	room=models.CharField(max_length=100)
	details=models.TextField()
	date_submitted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.type

# Create your models here.
