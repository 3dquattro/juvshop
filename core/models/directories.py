# Models for directories
from django.db import models
from datetime import datetime


class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name="Наименование")
    volumeCoefficient = models.FloatField(
        default=0,
        verbose_name="Коэффициент объема",
        help_text="Вычисляется как отношение объема модели среднего по размеру изделия, взятое из 3d-редактора к объему изделия реалистичных размеров.",
    )
    update_time = models.DateTimeField(
        blank=True, default=datetime.now, verbose_name="Время обновления"
    )
    status = models.IntegerField(default=0, verbose_name="Статус")

    def get_success_url(self):
        return "my/product_types"

    def __str__(self):
        return self.name

    pass


class Material(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name="Наименование")
    price = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Стоимость, руб/грамм"
    )
    density = models.FloatField(default=0, verbose_name="Плотность, кг/м^3")
    materialJSON = models.JSONField(
        verbose_name="JSON-представление материала для конструктора",
        help_text="Материал, заданный в форме JSON-строки, оформленной по стандартам ThreeJS для материалов.",
    )
    update_time = models.DateTimeField(
        blank=True, default=datetime.now, verbose_name="Время обновления"
    )
    status = models.IntegerField(default=0, verbose_name="Статус")

    def __str__(self):
        return self.name

    pass


class PartType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name="Наименование")
    productType = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, verbose_name="Тип изделия"
    )
    update_time = models.DateTimeField(
        blank=True, default=datetime.now, verbose_name="Время обновления"
    )
    status = models.IntegerField(default=0, verbose_name="Статус")

    def __str__(self):
        return self.name + " (" + str(self.pk) + ")"

    pass
