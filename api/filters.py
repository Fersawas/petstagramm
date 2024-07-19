from django_filters.rest_framework import FilterSet, filters
from pets.models import Pet


class PetsCategoryFilter(FilterSet):
    my_pets = filters.BooleanFilter(method='users_pet')

    def users_pet(self, queryset, name, value):
        user = self.request.user
        if value and not user.is_anonymous:
            return queryset.filter(owner=user)
        return queryset

    class Meta:
        model = Pet
        fields = ['category', ]
