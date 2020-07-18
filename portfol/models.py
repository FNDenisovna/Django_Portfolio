from django.db import models

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=100)
	descr = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfol/images/')
	ulr = models.URLField(blank=True)