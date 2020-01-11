from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static

from .viewsets import ProviderViewSet

router = routers.DefaultRouter()
router.register(r'api/common/provider', ProviderViewSet, basename='ProviderView')

urlpatterns = [
    path('', include(router.urls)), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 