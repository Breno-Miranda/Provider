from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from users.viewsets import BusinesViewSet, IndividualViewSet, CollaboratorUsersViewSet, PermissionViewSet, UsersViewSet

router = routers.DefaultRouter()
router.register(r'api/users/all', UsersViewSet, basename='UsersView')
router.register(r'api/users/search', UsersViewSet, basename='UsersViewSearch')
router.register(r'api/users/business', BusinesViewSet, basename='BusinesView')
router.register(r'api/users/collaborator', CollaboratorUsersViewSet, basename='CollaboratorView')
router.register(r'api/users/individual', IndividualViewSet, basename='IndividualView')
router.register(r'api/users/permission', PermissionViewSet, basename='PermissionView')


urlpatterns = [
    path('', include(router.urls)), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 