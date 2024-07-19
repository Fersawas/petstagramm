from django.db import models
from django.contrib.auth import get_user_model

from constants import MAX_LENGTH, SLUG_LENGTH


User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Категория'
    )
    slug = models.SlugField(
        max_length=SLUG_LENGTH,
        verbose_name='Слаг'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Pet(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Имя'
    )
    slug = models.SlugField(
        max_length=SLUG_LENGTH,
        verbose_name='Слаг'
    )
    image = models.ImageField(
        upload_to='media/',
        null=True,
        default=None,
        verbose_name='Изображение'
    )
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='pet',
        verbose_name='Категория'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Хозяин'
    )

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
