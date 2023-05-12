from django.db import models
from django.conf import settings


# Order model for personal area
class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    order_date = models.DateTimeField(null=True)
    update_time = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)
