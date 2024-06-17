from django.db import models

class Course(models.Model):
    course_title= models.TextField()
    course_description= models.TextField()
    course_start_date= models.DateField()
    course_end_date = models.DateField()
    code =models.PositiveSmallIntegerField()
    grading_system= models.CharField(max_length=20)
    course_materials= models.TextField()
# Create your models here.
