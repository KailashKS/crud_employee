from . import views
from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='emp_home'),
    path('employee_insert', EmployeeInsert.as_view(), name='emp_insert'),
    path('employee_view', EmployeeView.as_view(), name='emp_view'),
    path('delete/<pk>', EmployeeDelete.as_view(), name='emp_delete'),
    path('update/<pk>', EmployeeUpdate.as_view(), name='emp_update')
    # path('employee', views.employee, name="employee"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
