from django.db import models

class Class(models.Model):
    name = models.TextField()
    class_capacity = models.PositiveIntegerField()
    class_attendance = models.TextField()
    class_projects= models.TextField()
    class_activities= models.TextField()
    class_representatives= models.TextField()
    class_assignments= models.TextField()
    class_policies= models.TextField()
    class_requirements= models.TextField()
# Create your models here.
