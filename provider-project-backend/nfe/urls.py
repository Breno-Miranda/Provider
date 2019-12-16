from rest_framework import routers
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/nfe/emit', views.emit, name='emit' ),
    path('api/nfe/cancel', views.cancel, name='cancel' ),
]