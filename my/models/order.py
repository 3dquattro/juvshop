from django.db import models
from django.conf import settings
from datetime import datetime


# Order model for personal area
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, default=datetime.now)
    status = models.IntegerField(default=0)
    address = models.CharField(max_length=300, blank=False, default="Адрес не найден")

    """
    Свойство-представление для статуса заказа, 
    результат - кортеж из двух элементов:
    1. Текст, 2. Класс div-элемента bootstrap-badge
    """

    @property
    def status_representation(self) -> tuple:
        div_class = [
            "bg-primary",
            "bg-warning text-dark",
            "bg-info text-dark",
            "bg-warning",
            "bg-warning text-dark",
            "bg-success",
            "bg-light text-dark",
            "bg-danger",
        ]
        text = [
            "Создан",
            "Ожидает оплаты",
            "Оплачен",
            "В сборке",
            "Собран",
            "Отправлен",
            "Завершен",
            "Отклонен",
        ]
        return tuple([text[self.status], div_class[self.status]])
