from django_multitenant.utils import set_current_tenant
from .models import School
    
    
class MultitenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user and not request.user.is_anonymous:
            # TODO try catch block: if user has multiple tenants
            school = School.objects.get(user=request.user)
            set_current_tenant(school)
        return self.get_response(request)