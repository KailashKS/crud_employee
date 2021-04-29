from django.db import models
from django import forms

# Create your models here.


class Employee(models.Model):

    img = models.ImageField(upload_to='emp_img')
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    eval = models.CharField(default="Default", max_length=100)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    dept = models.TextField()
    remarks = models.TextField()
