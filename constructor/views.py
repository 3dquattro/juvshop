from django.views.generic.base import TemplateView
from django.conf import settings
from core.models import Material, ProductType, Jewelry
from api.serializers import JewelrySerializer, MaterialSerializer, ProductTypeSerializer

import logging


# CBV for jewelry constructor
class ConstructorView(TemplateView):
    template_name = "constructor/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if "idURL" in kwargs:
            logging.debug("id from url is not None")
            jewelry = Jewelry.objects.get(id=kwargs["idURL"])
            print("jewelry.user_id = " + str(jewelry.user_id))
            if jewelry.user_id == self.request.user.id:
                context["jewelry"] = JewelrySerializer(jewelry).data
                print(context["jewelry"])
            else:
                logging.error("id не совпадает")
        serializer_material = MaterialSerializer(Material.objects.all(), many=True)
        context["materials"] = serializer_material.data
        context["prtypes"] = ProductTypeSerializer(
            ProductType.objects.all(), many=True
        ).data
        # context['static_directory'] = settings.STATIC_ROOT
        return context
