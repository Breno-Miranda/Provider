from rest_framework import routers
from django.urls import path, include

from .viewsets import CampaignsViewset

router = routers.DefaultRouter()
router.register(r'api/campaign', CampaignsViewset , basename='CampaignsView')


urlpatterns = [
    path('', include(router.urls)),
]