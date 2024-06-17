from django.db import models

class Teacher(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    code =models.PositiveSmallIntegerField()
    email=models.EmailField()
    age= models.PositiveIntegerField()
    country= models.TextField()
    qualifications = models.TextField()
    hire_date = models.DateField()
    gender = models.TextField()
    bio = models.TimeField()
# Create your models here.
