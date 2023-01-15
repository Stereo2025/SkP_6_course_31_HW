from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.validators import check_birth_date


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=1000)
    role = models.CharField(max_length=9, choices=ROLES, default="member")
    age = models.PositiveIntegerField(null=True, blank=True)
    birth_date = models.DateTimeField(validators=[check_birth_date], null=True)
    email = models.EmailField(verbose_name='EmailAddress', blank=True,
                              validators=[RegexValidator(
                                  regex="@rambler.ru", inverse_match=True,
                                  message='Регистрация с домена rambler.ru запрещена.'
                              )])
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
