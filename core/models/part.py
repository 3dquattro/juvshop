from django.db import models
from .directories import PartType
from datetime import datetime


# Model for part
class Part(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70, verbose_name="Наименование")
    volume = models.FloatField(
        default=0, verbose_name="Объем", help_text="Берется из 3d-редактора"
    )
    category = models.ForeignKey(
        PartType, default=1, on_delete=models.CASCADE, verbose_name="Тип детали"
    )
    ModelFile = models.FileField(
        upload_to="parts/", verbose_name="Файл модели", help_text="В формате .obj"
    )
    update_time = models.DateTimeField(
        default=datetime.now, verbose_name="Время изменения"
    )
    status = models.IntegerField(default=0, verbose_name="Статус")

    def __str__(self):
        return (
            self.name + "," + self.category.productType.name + " (" + str(self.pk) + ")"
        )

    pass
