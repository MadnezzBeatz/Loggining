from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import LoginForm, RegisterForm
from .scripts.code import app_auth

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm
        return render(request, 'users/register.html', {'form': form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Super")
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/register.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm
        return render(request, 'users/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username= username, password = password)
            if user:
                login(request, user)
                messages.success(request, "Hola")
                return redirect('home')
        messages.error(request, f'Invalod')
        return render(request, 'users/login.html', {'form': form})




def sign_out(request):
    logout(request)
    messages.success(request, "You're out")
    return redirect('login')

def auth_app(request):

    username = request.GET.get("username",0)
    enteredpassword = request.GET.get("enteredpassword",0)
    resp = app_auth(username, enteredpassword)
    # print(resp)
    return HttpResponse(f"{resp}")





# Create your views here.
