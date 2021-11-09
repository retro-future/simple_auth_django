from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class MyAccountManager(BaseUserManager):
    """
        Manager for CustomAuthUser
    """

    def creat_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomAuthUser(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"

    objects = MyAccountManager()

    def __str__(self):
        return self.username
