from django.urls import path 
from .views import *

urlpatterns = [
    path('home', home),
     path('sites', sites, name='sites'),
    path('dept', departments, name='scope_departments'),
    # path('programs', programs),
    # path('my_schools', my_schools),
    
]