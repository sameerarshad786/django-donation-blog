from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import UserRegisterForm
from .models import User


def SignIn(request):
    if request.user.is_authenticated:
        return redirect("home-page")

    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password").lower()

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'Username OR password does not exit')
        
    context = {
        "title": "Sign In"
    }

    return render(request, "users/signin.html", context)

def SignUp(request):
    if request.user.is_authenticated:
        return render(request, "404.html")
    elif request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")

    else:
        form = UserRegisterForm()

    context = {
        "form": form,
        "title": "Register"
    }

    return render(request, "users/signup.html", context)

def profile(request):
    return render(request, "users/profile.html")
