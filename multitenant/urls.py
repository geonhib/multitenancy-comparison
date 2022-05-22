from django.urls import path
from .views import SchoolList, DepartmentList, ProgramList, departments

urlpatterns = [
    path('schools', SchoolList.as_view(), name='schools'), 
    path('departments', DepartmentList.as_view()),
    path('programs', ProgramList.as_view()),

    path('dept', departments, name='multitenant_departments'),

]