from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomAuthUser(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
