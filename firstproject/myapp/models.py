from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    class_name=models.CharField(max_length=100)
    roll=models.IntegerField()
    def __str__(self):
        return self.name
    

class Teacher(models.Model):
     name=models.CharField(max_length=100)
     department=models.CharField(max_length=100)
     emails=models.CharField(max_length=100)
     def __str__(self):
         return self.name