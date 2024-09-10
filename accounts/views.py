from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from dashboard.libs import get_general_settings
# Create your views here.
from django.conf import settings
BASE_DIR = settings.BASE_DIR

def index(request):
    return redirect('Login')

def Login(request):
    file_path = str(BASE_DIR / 'dashboard/settings.json')
    settings, img_obj = get_general_settings(file_path)
    if request.method == 'POST':
        login_type = request.POST.get('type')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if login_type == '2':
            users = User.objects.filter(email=email)
        else:
            users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            username = user.username
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:

                has_userprofile = False
                is_employee = False
                try:
                    userprofile = user.userprofile
                    has_userprofile = True
                except:pass
                if has_userprofile:
                    is_employee = userprofile.profile_type == '2' or userprofile.profile_type == '1'
            
                if is_employee or user.is_superuser:
                    login(request, user)
                    return redirect('PanelHome')

    return render(request, 'accounts/login/login.html', {'img_obj':img_obj, 'settings':settings})

def Logout(request):
    logout(request)
    return redirect('Login')