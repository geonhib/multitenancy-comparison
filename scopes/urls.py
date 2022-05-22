from django.urls import path 
from .views import *

urlpatterns = [
    path('home', home),
     path('sites', sites),
    path('dept', departments),
    # path('programs', programs),
    # path('my_schools', my_schools),
    
]