"""customjuvshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from catalog.views import CatalogIndexView

urlpatterns = [
    # Include for an "api" app (file urls.py)
    path("api/", include("api.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    # Path for constructor view
    path("constructor/", include("constructor.urls")),
    path("my/", include("my.urls")),
    path("catalog/", include("catalog.urls")),
    path("", CatalogIndexView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
