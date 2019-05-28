from django.db import models
from course.models import Course
courses = models.ManyToManyField(Course)

class Student(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length = 20)
	registration_number = models.CharField(max_length = 20)
	emails = models.EmailField(max_length = 70)
	phone_number = models.CharField(max_length = 10)
	date_joined = models.DateField()




# Create your models here.
