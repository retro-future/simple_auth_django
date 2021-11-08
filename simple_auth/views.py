from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from simple_auth.forms import CustomAuthUserForm, RegistrationForm


def home(request):
    return render(request, "home.html")


def success_register(request):
    return render(request, "register_done.html")


def custom_login(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = CustomAuthUserForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthUserForm()
    context["form"] = form
    return render(request, "login_page.html", context)


def custom_logout(request):
    logout(request)
    return redirect("home")


def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reg_done")
        else:
            context["form"] = form
    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, "registration_page.html", context)
