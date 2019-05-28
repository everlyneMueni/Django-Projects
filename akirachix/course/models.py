from django.db import models

from teacher.models import Teacher
teacher = models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)



class Course(models.Model):
	name = models.CharField(max_length = 20)
	duration_in_months = models.IntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField()


# Create your models here.
