from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'username': request.user.username})

@login_required
def profile(request):
    return render(request, 'profile.html', {
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login,
    })
