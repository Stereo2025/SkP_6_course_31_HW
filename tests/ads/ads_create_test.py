import pytest
from rest_framework import status

from ads.models import Ad


@pytest.mark.django_db
def test_ads_create(client, user, category, user_token):
    data = {
        "name": "new test ad",
        "price": 10,
        "description": "test description",
        "is_published": False,
        "author": user.id,
        "category": category.id
    }
    assert not Ad.objects.count()

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + user_token
    )
    assert response.status_code == status.HTTP_201_CREATED

    new_ad = Ad.objects.last()
    assert response.data == {
        'id': new_ad.id,
        'author': user.id,
        'category': category.id,
        'description': data['description'],
        'image': None,
        'is_published': data['is_published'],
        'name': data['name'],
        'price': data['price'],
    }