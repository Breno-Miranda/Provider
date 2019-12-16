from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url('api/auth', views.Authentication.auth, name='auth'),
    url('api/checkout-auth', views.Authentication.check_auth, name='auth'),
    url('api/register-user-token', views.Authentication.register_user_token, name='auth'),
    url('api/company-token', views.Authentication.company_token, name='auth'),
    
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 