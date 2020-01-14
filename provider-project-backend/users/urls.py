from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from users.viewsets import ProfileViewSet, PermissionViewSet,UsersViewSet, UserAccountViewSet, UserContactViewSet

router = routers.DefaultRouter()
router.register(r'api/users/all', UsersViewSet, basename='UsersView')
router.register(r'api/users/search', UsersViewSet, basename='UsersViewSearch')
router.register(r'api/users/profile',
                ProfileViewSet,
                basename='ProfileView')
router.register(r'api/users/permission',
                PermissionViewSet,
                basename='PermissionView')

router.register(r'api/users/account',
                UserAccountViewSet,
                basename='UserAccountView')
router.register(r'api/users/contact',
                UserContactViewSet,
                basename='UserContactView')

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
