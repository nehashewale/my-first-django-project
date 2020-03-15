from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_number = models.IntegerField()
    city = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    registartion_number = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name 

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    employee_id = models.IntegerField()
    city = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.first_name 
