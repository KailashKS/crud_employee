from django.shortcuts import render, redirect
from django.http import HttpResponse
import base64
from django.core.files.storage import FileSystemStorage
from .forms import EmpForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Employee
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    return render(request, "home.html")


class EmployeeInsert(CreateView):
    model = EmpForm()

    def post(self, request):
        form = EmpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp_insert')
        else:
            return render(request, 'error.html')

    def get(self, request):
        form = EmpForm()
        return render(request, 'employee_insert.html', context={'form': form})


class EmployeeView(ListView):
    def get(self, request):
        # form = EmpForm()
        employee = Employee.objects.all()
        return render(request, 'employee_view.html', context={'emp_details': employee})


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('emp_view')


class EmployeeUpdate(UpdateView):
    model = Employee
    employee = Employee.objects.all()
    extra_context = {'emp_details': employee}
    template_name = 'employee_update.html'
    form_class = EmpForm
    success_url = reverse_lazy('emp_view')
