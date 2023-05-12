from django.db import models
from .profile import Profile


class Address(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="Профиль пользователя"
    )
    address = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Адрес"
    )
