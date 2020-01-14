from rest_framework import routers
from django.urls import path, include

from .viewsets import LotsViewset

router = routers.DefaultRouter()
router.register(r'api/lot', LotsViewset , basename='LotsView')


urlpatterns = [
    path('', include(router.urls)),
]