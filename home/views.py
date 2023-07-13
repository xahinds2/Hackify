from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


@login_required
def home(request):
    return render(request, 'home.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username).first()
        if user:
            return render(request, 'signup.html')

        User.objects.create(username=username, password=password, email=email)
        return redirect('login')

    return render(request, 'signup.html')


def custom_logout(request):
    logout(request)
    return redirect('login')
