from django.urls import path
from .views import get_employees, create_employee, get_employee, update_employee, delete_employee

urlpatterns = [
    path('api/employees/', get_employees, name='get_employees'),  # GET all employees
    path('api/employees/create/', create_employee, name='create_employee'),  # ✅ POST new employee
    path('api/employees/<int:pk>/', get_employee, name='get_employee'),  # GET single employee
    path('api/employees/<int:pk>/update/', update_employee, name='update_employee'),  # PUT update employee
    path('api/employees/<int:pk>/delete/', delete_employee, name='delete_employee'),  # DELETE employee
]
