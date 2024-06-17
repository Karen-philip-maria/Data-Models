from django.db import models

class Students(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    code =models.PositiveSmallIntegerField()
    email=models.EmailField()
    age= models.PositiveIntegerField()
    country= models.TextField()
    phone_number=models.PositiveIntegerField()
    date_of_birth= models.DateField()
    immediate_contact = models.DateField()
    bio = models.TextField()
# Create your models here.
