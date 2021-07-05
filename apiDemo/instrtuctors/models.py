from django.db import models

# Create your models here.
class Instructor(models.Model):
	name = models.CharField(max_length=100)
	dept_name = models.CharField(max_length=100)
	salary = models.IntegerField()
	age = models.IntegerField()
	dependants = models.IntegerField()

