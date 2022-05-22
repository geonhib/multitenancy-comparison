from django.http import HttpRequest
from django_scopes import scopes_disabled
from django.urls import get_script_prefix

from django_scopes import scope
from .models import Site


def ignore_scopes_in_admin_middleware(get_response, admin_path: str="admin"):
    """Disables scoping in dango admin"""
    def middleware(request: HttpRequest):
        if request.path.startswith(get_script_prefix() + admin_path):
            with scopes_disabled():
                return get_response(request)

        return get_response(request)

    return middleware


# class ScopingMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         get_tenant = Site.objects.get(user=request.user)
#         print(get_tenant)
#         with scope(tenant=get_tenant):
#             return self.get_response(request)


def ignore_scopes_if_superuser(get_response):
    """Disables scoping if user is superuser"""
    def middleware(request: HttpRequest):
        if request.user.is_superuser:
            with scopes_disabled():
                return get_response(request)
        else:
            pass
            # TODO scope if user is not superuser
            return get_response(request)

    return middleware
