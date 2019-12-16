from rest_framework import routers
from django.urls import path, include
from product.viewsets import ProductViewSet, NewProductViewSet

router = routers.DefaultRouter()
router.register(r'api/products', ProductViewSet , basename='Products')
router.register(r'api/products/new', NewProductViewSet , basename='product-new')



urlpatterns = [
    path('', include(router.urls)),
]