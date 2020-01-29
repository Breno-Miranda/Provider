from rest_framework import routers
from django.urls import path, include

from .viewsets import ItensViewSet, RequestViewSet, StatusViewSet,requestsFromPdfViewSet, routineRequestsSumItensViewSet

router = routers.DefaultRouter()
router.register(r'api/request', RequestViewSet , basename='RequestViewSet')
router.register(r'api/request/itens', ItensViewSet , basename='ItensViewSet')
router.register(r'api/request/status', StatusViewSet , basename='StatusViewSet')
router.register(r'api/request/print/pdf', requestsFromPdfViewSet , basename='requestsFromPdfViewSet')


#  rotinas para consertos via code.
router.register(r'api/request/routine/settings-value-total-request', routineRequestsSumItensViewSet , basename='routineRequestsSumItensViewSet')




urlpatterns = [
    path('', include(router.urls)),
]