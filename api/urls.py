from django.urls import path
from .views import (
    api_materials_list,
    api_product_type_list,
    api_part_types_for_product,
    api_jewelry,
    api_parts_for_category,
    api_partts_as_object,
    api_single_part,
)

urlpatterns = [
    path("materials/", api_materials_list),
    path("producttypes/", api_product_type_list),
    path("parttypes/<int:producttype>", api_part_types_for_product),
    path("pttypes/<int:producttype>", api_partts_as_object),
    path("part/<int:sid>", api_single_part),
    path("jewelry/", api_jewelry),
    path("jewelry/<int:id>", api_jewelry),
    path("parts/<int:category>", api_parts_for_category),
]
