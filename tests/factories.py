import factory

from ads.models import Category, Ad
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')
    slug = factory.Faker("ean", length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    name = factory.Faker('name')
    price = 10
