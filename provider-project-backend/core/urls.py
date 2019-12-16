from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include('authentication.urls')),
    path('', include('users.urls')),
    path('', include('product.urls')),
    path('', include('sale.urls')),
    path('', include('request.urls')),
    path('', include('nfe.urls')),
    path('', include('company.urls')),
    path('', include('information.urls')),
    path('admin/', admin.site.urls),
]
