from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static

from .viewsets import CompanyViewSet, CatalogsCompanyViewSet

router = routers.DefaultRouter()
router.register(r'api/companys/catalog', CatalogsCompanyViewSet, basename='catalogView')
router.register(r'api/companys', CompanyViewSet, basename='CompanyView')

urlpatterns = [
    path('', include(router.urls)), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 