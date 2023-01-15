import pytest


@pytest.mark.django_db
def test_ads_create(client, user, category, user_token):
    expected_response = {
        'id': 1,
        'author': user.id,
        'category': category.id,
        'description': 'test description',
        'image': None,
        'is_published': False,
        'name': 'new test ad',
        'price': 10,
    }
    data = {
        "name": "new test ad",
        "price": 10,
        "description": "test description",
        "is_published": False,
        "author": user.id,
        "category": category.id
    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + user_token
    )
    assert response.status_code == 201
    assert response.data == expected_response
