from django.contrib import admin
from django.utils.safestring import mark_safe

from pets.models import Category, Pet


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
    ]


@admin.register(Pet)
class PetModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'owner',
        'category',
        'get_image'
    ]

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}"'
                             'style="max-height: 150px">')
        except Exception:
            return None

    get_image.short_description = 'Изображение'
