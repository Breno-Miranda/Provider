from rest_framework import routers
from django.urls import path, include


from .viewsets import PaymentFormViewSet, FlagsCardViewSet, AccreditingViewSet, NatureOperationViewSet, SaleViewSet

router = routers.DefaultRouter()
router.register(r'api/sale', SaleViewSet , basename='SaleViewSet')
router.register(r'api/sale/flags-card', FlagsCardViewSet , basename='FlagsCardViewSet')
router.register(r'api/sale/accrediting', AccreditingViewSet , basename='AccreditingViewSet')
router.register(r'api/sale/pymente-form', PaymentFormViewSet , basename='PaymentFormViewSet')
router.register(r'api/sale/nature-operation', NatureOperationViewSet , basename='NatureOperationViewSet')

urlpatterns = [
    path('', include(router.urls)),
]