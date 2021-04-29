from django.shortcuts import render, redirect
from django.http import HttpResponse
import base64
from django.core.files.storage import FileSystemStorage
from .forms import EmpForm
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from .models import Employee
from django.urls import reverse_lazy

# Create your views here.


def base(request):
    return render(request, "base.html")


class EmployeeInsert(FormView):
    model = EmpForm()

    def post(self, request):
        form = EmpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('emp_insert')

    def get(self, request):
        form = EmpForm()
        return render(request, 'employee_insert.html', context={'form': form})

# def employee(request):
#     form = EmpForm()
#     return render(request, 'employee.html', {'form': form})


class EmployeeView(ListView):
    def get(self, request):
        form = EmpForm()
        employee = Employee.objects.all()
        return render(request, 'employee_view.html', context={'emp_details': employee, 'form': form})


class EmployeeDelete(DeleteView):
    def get(self, request):
        return HttpResponse("Hello World")
    # def get(self, request, id=None):
    #     Employee.objects.filter(id=id).delete()
    #     return render(request, 'employee_view.html', context={'emp_details': employee, 'form': form})
