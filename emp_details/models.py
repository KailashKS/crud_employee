from django.db import models
from django import forms
from django.utils import timezone
from datetime import datetime
from django.db.models import F, Q
from django.contrib import messages

# Create your models here.


class Employee(models.Model):

    img = models.ImageField(upload_to='emp_img')
    name = models.CharField(max_length=100)
    dob = models.DateField()
    doj = models.DateField()
    gender = models.CharField(max_length=6)
    eval = models.CharField(max_length=200, blank=True, null=True)
    insurance = models.BooleanField(default=False)
    salary = models.FloatField(default=0.0)
    dept = models.TextField()
    remarks = models.TextField()

    def clean(self):
        import datetime
        if not (datetime.date.today() - self.dob) > datetime.timedelta(days=18*365):
            raise forms.ValidationError('Age less than 18')
