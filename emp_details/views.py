from django.shortcuts import render, redirect
from django.http import HttpResponse
import base64
from django.core.files.storage import FileSystemStorage
from .forms import EmpForm

# Create your views here.


def base(request):
    return render(request, "base.html")


def employee(request):
    form = EmpForm()
    return render(request, 'employee.html', {'form': form})
