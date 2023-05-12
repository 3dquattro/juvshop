from django.urls import path
from .views import ConstructorView

urlpatterns = [
    path("", ConstructorView.as_view()),
    path("<int:idURL>", ConstructorView.as_view()),
]
