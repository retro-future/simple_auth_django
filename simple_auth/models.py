from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class MyAccountManager(BaseUserManager):
    """
        Manager for CustomAuthUser
    """

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Email address")
        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomAuthUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(verbose_name="username", max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
