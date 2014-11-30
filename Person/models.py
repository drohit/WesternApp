from django.db import models
from Course.models import Course
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
	user = models.OneToOneField(User) #allows login/logout capabilities using Django's built-in user class
	name = models.CharField(max_length=30)
	year = models.IntegerField(null=True, blank=True)
	email = models.CharField(max_length=40)
	courses = models.ManyToManyField(Course, null=True, blank=True)
	residence = models.CharField(max_length=28, null=True, blank=True)

REZ_CHOICES = []
