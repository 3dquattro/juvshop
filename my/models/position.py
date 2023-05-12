from django.db import models
from core.models import Jewelry
from .order import Order
from .cart import *


# Модель позиции заказа
class Position(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="Заказ", blank=True, null=True
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="Корзина", blank=True, null=True
    )
    jewelry = models.ForeignKey(Jewelry, default=1, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Количество", default=1)
    price = models.FloatField(default=0)
    pass
