"""
Definition of models.
"""

from django.db import models

# Create your models here.
class testdata(models.Model):
	id = models.IntegerField(default=170)
	type =  models.CharField(max_length=20)
	source = models.CharField(max_length=20)
	total = models.IntegerField(default=200)
	
