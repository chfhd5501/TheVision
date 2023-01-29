from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from argon2 import PasswordHasher
from common.forms import UserForm
from thevision.models import Group

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('question_list')
    else:
        form = UserForm
    return render(request, 'common/signup.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'common/login.html')

def logout_view(request):
    logout(request)
    return redirect('common:login')





