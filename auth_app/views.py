from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/index')
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'Passwords do not match')
            return redirect('/auth/register')

        if len(username.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Invalid username or password')
            return redirect('/auth/register')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'User already exists, please, try another username')
            return redirect('/auth/register')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/auth/login')

        except:
            messages.add_message(request, constants.ERROR, 'Server error, try again')
            return redirect('/auth/register')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/index')
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        username = auth.authenticate(username=username, password=password)

        if not username:
            messages.add_message(request, constants.ERROR, 'Invalid user or password')
            return redirect('/auth/login')
        else:
            auth.login(request, username)
            return redirect('/index')
            
def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
