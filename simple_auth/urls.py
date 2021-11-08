from django.urls import path

from simple_auth.views import home, custom_login, registration_view, success_register, custom_logout

urlpatterns = [
    path("login/", custom_login, name='login'),
    path("logout/", custom_logout, name="logout"),
    path("register/", registration_view, name='register'),
    path("home/", home, name='home'),
    path("register_done/", success_register, name='reg_done'),
]
