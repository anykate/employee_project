from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})


def save_employee(request, emp_id=0):
    if emp_id:
        employee = get_object_or_404(Employee, id=emp_id)
        form = EmployeeForm(request.POST or None, instance=employee)

    else:
        form = EmployeeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('employees:index')

    return render(request, 'employees/add_update.html', {'form': form})


def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    employee.delete()
    return redirect('employees:index')
