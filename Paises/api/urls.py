from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .viewsets import PaisViewSet

router = DefaultRouter()

router.register(prefix="paises", viewset= PaisViewSet)


urlpatterns = [
    path("api/", include(router.urls))
]
