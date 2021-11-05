from django.urls import path

from simple_auth.views import home, custom_login, registration_view, success_register

urlpatterns = [
    path("login/", custom_login, name='login'),
    path("register/", registration_view, name='register'),
    path("home/", home, name='home'),
    path("register_done/", success_register, name='reg_done'),
]