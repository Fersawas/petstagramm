from django.urls import include, path
from rest_framework import routers

from api.views import CategoryViewSet, UserPetsViewSet, PetsViewSet

router = routers.SimpleRouter()

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'user_pets', UserPetsViewSet, basename='user_pets')
router.register(r'pets', PetsViewSet, basename='pets')


urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('djoser.urls')),
    path('users/', include('djoser.urls.jwt'))
]
