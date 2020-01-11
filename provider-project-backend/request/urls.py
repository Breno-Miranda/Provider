from rest_framework import routers
from django.urls import path, include

from .viewsets import ItensViewSet, RequestViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register(r'api/request', RequestViewSet , basename='RequestViewSet')
router.register(r'api/request/itens', ItensViewSet , basename='ItensViewSet')
router.register(r'api/request/status', StatusViewSet , basename='StatusViewSet')

urlpatterns = [
    path('', include(router.urls)),
]