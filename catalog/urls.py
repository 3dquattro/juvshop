from django.urls import path
from .views import CatalogIndexView, JewelryCardView

urlpatterns = [
    path("", CatalogIndexView.as_view()),
    path("<int:page>", CatalogIndexView.as_view()),
    path("jewelry/<int:jid>", JewelryCardView.as_view()),
]
