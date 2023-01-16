import pytest
from rest_framework import status


@pytest.mark.django_db
def test_selection_create(client, user_token, user, ad):
    response = client.post("/selection/create/",
                           {
                               "name": "test",
                               "owner": user.id,
                               "items": [ad.id]
                           },
                           content_type="application/json",
                           HTTP_AUTHORIZATION='Bearer ' + user_token)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        'id': 1,
        'name': 'test',
        'owner': user.id,
        'items': [ad.id]
    }
