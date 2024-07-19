import base64
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import serializers

from pets.models import Category, Pet


User = get_user_model()


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PetsSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Pet
        fields = '__all__'


class UserMainSerializer(serializers.ModelSerializer):
    pets = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'pets',
            'email'
        ]

    def get_pets(self, user):
        pets = Pet.objects.filter(owner=user)
        return PetsSerializer(pets, many=True, context=self.context).data
