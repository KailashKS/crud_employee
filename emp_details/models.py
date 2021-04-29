from django.db import models

# Create your models here.


class Employee(models.Model):
    gender = {
        'Male': '1',
        'Female': '2',
        'Others': '3'
    }

    eval = {
        'Passed Psych Evaluation 1': '1',
        'Passed Psych Evaluation 2': '2',
        'Passed Physical Evaluation': '3'
    }
    img = models.ImageField(upload_to='emp_img')
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.IntegerField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    dept = models.TextField()
    remarks = models.TextField()
