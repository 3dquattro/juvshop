from django.db import models
from django.conf import settings
from .order import Order
from datetime import datetime


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Sender"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    send_date = models.DateTimeField(blank=True, default=datetime.now)
