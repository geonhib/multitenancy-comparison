from django.shortcuts import render
from django.views.generic import ListView
from .models import School, Department, Program
from django_multitenant.utils import set_current_tenant


class SchoolList(ListView):
    model = School
    template_name = 'schools.html'
    context_object_name = 'tenants'


class DepartmentList(ListView):
    model = Department
    template_name = 'departments.html'
    context_object_name = 'departments'


class ProgramList(ListView):
    model = Program
    template_name = 'programs'
    context_object_name = 'programs'



def departments(request):
    if request.user.is_superuser:
        print("super")
        departments = Department.objects.all()
    else:
        print("staff")
        school = School.objects.get(user=request.user)
        set_current_tenant(school)
        departments = Department.objects.all()

    dept_num = departments.count()
    context = {
        "departments": departments,
        "dept_num": dept_num,
    }
    return render(request, 'departments.html', context)