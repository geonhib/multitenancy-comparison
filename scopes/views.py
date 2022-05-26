
from django.shortcuts import render
from .models import Site, Department, Program
from django_scopes import scope
from django_scopes import scopes_disabled


def home(request):
    return render(request, 'base.html')


def sites(request):
    sites = Site.objects.all()
    print(sites)
    context = {
        'tenants': sites
    }
    return render(request, 'schools.html', context)


@scopes_disabled()
def departments(request):
    if request.user.is_superuser:
        with scope(site=None):
            departments = Department.objects.all()
    else:
        tenant = Site.objects.get(user=request.user)
        with scope(site=tenant):
            departments = Department.objects.all()

    print(departments)   
    dept_num = departments.count()
    print(departments.count())
    context = {
        'departments': departments,
        'dept_num': dept_num,
        # 'tenant': tenant,
    }
    return render(request, 'departments.html', context)


def my_schools(request):
    schools = Site.objects.filter(user=request.user)
    context = {
        'schools': schools
    }
    return render(request, 'my_schools.html', context)


def get_tenant(request):
    if request.method == 'program':
        tenant = request.program.get('school')
        print(tenant)
        context = {
            'tena': tenant
        }
        return render(request, 'home.html', context)






