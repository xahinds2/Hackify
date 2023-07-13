from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as log, logout


@login_required
def view_hacks(request):
    return render(request, 'viewhacks.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            log(request, user)
            return redirect('view_hacks')

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
        return redirect('login_user')

    return render(request, 'signup.html')
