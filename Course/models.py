from django.db import models

# Create your models here.
class Course(models.Model):
	subject = models.CharField(max_length=250)
	number = models.IntegerField()
	term = models.CharField(max_length=20)
	title = models.TextField()