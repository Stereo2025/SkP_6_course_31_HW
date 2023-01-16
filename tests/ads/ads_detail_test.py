import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ads_create(client, ad, user_token):
    expected = {
        "id": ad.id,
        "author": ad.author.pk,
        "name": ad.name,
        "price": ad.price,
        "description": ad.description,
        "is_published": False,
        "category": ad.category.name,
        "image": ad.image.url if ad.image else None
    }
    response = client.get(
        f"/ad/{ad.id}/",
        HTTP_AUTHORIZATION="Bearer " + user_token)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected
