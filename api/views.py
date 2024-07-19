from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from pets.models import Category, Pet
from api.serializers import (CategorySerializer, UserMainSerializer,
                             PetsSerializer)
from api.permissions import IsOwnerOrRead
from api.filters import PetsCategoryFilter


User = get_user_model()


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserPetsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserMainSerializer


class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer
    permission_classes = [IsOwnerOrRead, IsAuthenticatedOrReadOnly]
    filterset_class = PetsCategoryFilter

    def perform_create(self, serializer):
        return serializer.save(
            owner=self.request.user
        )
