import pytest
from rest_framework import status

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads_factories = AdFactory.create_batch(4)

    response = client.get("/ad/")

    ads = []
    for ad in ads_factories:
        ads.append({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": ad.author.first_name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else None,
        })

    expected_response = {
        "items": ads,
        "num_pages": 1,
        "total": 4,
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response
