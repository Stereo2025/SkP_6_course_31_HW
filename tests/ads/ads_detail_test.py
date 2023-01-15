import pytest


@pytest.mark.django_db
def test_ads_create(client, ad, user_token):
    expected = {
        'id': 2,
        'name': '',
        'category': '',
        'author': 3,
        'price': 10,
        'description': None,
        'is_published': False,
        'image': None
    }
    response = client.get(
        f"/ad/{ad.id}/",
        HTTP_AUTHORIZATION="Bearer " + user_token)

    assert response.status_code == 200
    assert response.data == expected
