from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from simple_auth.forms import CustomAuthUserForm, RegistrationForm, UserUpdateForm


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
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect('home')
        else:
            messages.error(request, "Please write credentials correct")
    else:
        form = CustomAuthUserForm()
    context["form"] = form
    return render(request, "login_page.html", context)


def custom_logout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("home")


def registration_view(request):
    """
     Renders Registration Form
    """
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pass)
            login(request, account)
            messages.success(request, "You have been Registered as {}".format(request.user.username))
            return redirect("reg_done")
        else:
            messages.error(request, "Please Correct Below Errors")
            context["form"] = form
    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, "registration_page.html", context)


def account_view(request):
    """
    Renders userprofile page
    """

    if not request.user.is_authenticated:
        return redirect("login")
    context = {}

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "profile Updated")
        else:
            messages.error(request, "Please Correct Below Errors")
    else:
        form = UserUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username
            }
        )
    context['form'] = form
    return render(request, "userprofile.html", context)