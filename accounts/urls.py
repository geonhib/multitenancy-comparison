from django.urls import path, include
from .views import logout_view

urlpatterns = [

    path("auth/", include("django.contrib.auth.urls")),  
    path('logout_view/', logout_view, name='logout_view')

]