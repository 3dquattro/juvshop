# Модель изделия
from django.db import models
from .directories import ProductType, Material
from django.conf import settings
from .part import Part
from datetime import datetime


class Jewelry(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=120, verbose_name="Наименование")
    parts = models.ManyToManyField(
        Part,
        verbose_name="Детали",
        help_text='Поле "многие ко многим", необходимый набор деталей выбирается нажатием.',
    )
    ispublic = models.BooleanField(
        default=False,
        verbose_name="Публичное изделие?",
        help_text="Характеризует необходимость отображения изделия в каталоге.",
    )
    type = models.ForeignKey(
        ProductType, default=1, on_delete=models.SET_DEFAULT, verbose_name="Тип изделия"
    )
    material = models.ForeignKey(
        Material, default=1, on_delete=models.SET_DEFAULT, verbose_name="Материал"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    preview = models.ImageField(
        upload_to="previews/", blank=True, verbose_name="Изображение"
    )
    update_time = models.DateTimeField(
        blank=True, default=datetime.now, verbose_name="Время обновления"
    )
    status = models.IntegerField(default=0, verbose_name="Статус")
    weight = models.FloatField(default=0, null=True, verbose_name="Вес")
    cost = models.FloatField(default=0, null=True, verbose_name="Стоимость")
    is_editable = models.BooleanField(default=True, verbose_name="Редактируемо?")

    def _get_cost(self):
        price = float(self.material.price)
        return self.weight * price

    def _get_weight(self):
        weight = 0
        coefficient = self.type.volumeCoefficient
        density = self.material.density
        for part in self.parts.all():
            weight += part.volume * coefficient * density
        return weight

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.weight = self._get_weight()
            self.cost = self._get_cost()
        super(Jewelry, self).save(*args, **kwargs)

    def copy(self):
        result = Jewelry()
        for field in Jewelry._meta.fields:
            if field.name not in ["parts", "id"]:
                result.__setattr__(field.name, self.__getattribute__(field.name))
        result.pk = None
        result.save()
        result.parts.set(self.parts.all())
        return result

    pass
