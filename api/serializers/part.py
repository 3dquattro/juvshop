from core.models.part import Part
from rest_framework import serializers


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = "__all__"

    pass


class PartSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ["id", "name"]

    pass
