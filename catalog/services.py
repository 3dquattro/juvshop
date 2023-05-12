from core.models import Jewelry
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def context_catalog(page: int) -> dict:
    context = {}
    jewelry = (
        Jewelry.objects.filter(ispublic=True)
        .order_by("name")
        .values("id", "name", "material__name", "type__name", "preview")
    )
    paginator = Paginator(object_list=jewelry, per_page=10, allow_empty_first_page=True)
    page_obj = paginator.get_page(page)
    context["page"] = page_obj
    context["page_range"] = list(paginator.get_elided_page_range())
    return context


def context_jewelry_card(id: int) -> dict:
    context = {}
    context["jewelry"] = get_object_or_404(Jewelry, pk=id)
    context["material"] = context["jewelry"].material.name
    return context
