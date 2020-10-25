import pytest
from rest_framework import status


@pytest.mark.django_db
def test_user_list_response(create_valid_user, user_client):
    """
    Ensure we can connect to user list url.
    """
    create_valid_user
    url = "/api/v1/users/"
    response = user_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.runt
def test_single_user_response(create_valid_user, user_client):
    """
    Ensure we can connect to single user url.
    """
    user = create_valid_user
    url = f"/api/v1/users/{user.pk}/"
    response = user_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_error_response(user_client):
    """
    Ensure we get error 404 while trying to connect to non-exist user url.
    """
    response = user_client.get("/api/v1/users/1/user/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_post_user_success(user_client):
    """
    Ensure we can add new user.
    """
    response = user_client.post(
        "/api/v1/users/",
        {"email": "email@mail.com", "password": "S_t_r_o_n_g"},
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_user_fail(create_valid_user, user_client):
    """
    Ensure we can't add new user without password.
    """
    create_valid_user
    response = user_client.post(
        "/api/v1/users/",
        {"email": "email@mail.com"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
