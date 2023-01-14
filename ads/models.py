from django.core.validators import MinLengthValidator
from django.db import models

from ads.validators import not_published
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=10, unique=True,
                            validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=False, validators=[not_published])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='pictures/')

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
