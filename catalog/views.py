from django.views.generic.base import TemplateView
from .services import *


class CatalogIndexView(TemplateView):
    def get_template_names(self):
        return "catalog/index.html"

    # Rendering template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_num = int(kwargs["page"]) if "page" in kwargs else 1
        context.update(context_catalog(page_num))
        return context


class JewelryCardView(TemplateView):
    template_name = "catalog/jewelry.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        jewelry_id = int(kwargs["jid"]) if "jid" in kwargs else 0
        context.update(context_jewelry_card(jewelry_id))
        return context
