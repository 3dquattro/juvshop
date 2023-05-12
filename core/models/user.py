# Переопределение модели пользователя, для логина по адресу почты
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from my.models import *


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email - обязательное поле")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        # Creating user cart
        cart = Cart()
        cart.user = user
        cart.save()
        # Creating user profile
        profile = Profile()
        profile.user = user
        profile.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    create_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    status = models.IntegerField(default=0)
    name = models.CharField(
        blank=True, default="", max_length=150, verbose_name="Имя (для отображения)"
    )
    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin
