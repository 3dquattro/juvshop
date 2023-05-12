from core.models.jewelry import Jewelry
from rest_framework import serializers


class JewelrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = ["id", "name", "parts", "type", "material", "user"]

    # Валидатор для поля имени изделия
    def validate_name(self, data):
        if len(data) > 150:
            return data[:150]

    pass
