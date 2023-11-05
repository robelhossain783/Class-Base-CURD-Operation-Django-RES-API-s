from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    subject = models.CharField(max_length=50)
    email = models.CharField(max_length=50)