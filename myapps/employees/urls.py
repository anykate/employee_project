from django.urls import path
from . import views


app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save_employee, name='add_employee'),
    path('save/<int:emp_id>/', views.save_employee, name='update_employee'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
]
