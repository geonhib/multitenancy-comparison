from django.shortcuts import redirect, render

# Create your views here.
def logout_view(request):
    request.session.clear()
    return redirect('login')