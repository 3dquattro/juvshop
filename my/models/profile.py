from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70, default="-")
    last_name = models.CharField(max_length=70, default="-")
    second_name = models.CharField(max_length=70, default="-")
    birthdate = models.DateField(blank=True, null=True)
    active_address = models.ForeignKey(
        to="my.Address",
        null=True,
        related_name="addresses",
        on_delete=models.SET_NULL,
        blank=True,
    )
    pass
