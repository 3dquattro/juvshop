from core.models.directories import Material, ProductType, PartType
from rest_framework import serializers


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"

    pass


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"

    pass


class PartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartType
        fields = ["id", "name"]

    pass
