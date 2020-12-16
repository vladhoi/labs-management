import pytest
from rest_framework import status


@pytest.mark.django_db
def test_user_list_response(create_valid_user, user_client):
    """
    Ensure we can connect to user list url.
    """
    url = "/api/v1/users/"
    response = user_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.runt
def test_single_user_response(create_valid_user, user_client):
    """
    Ensure we can connect to single user url.
    """
    url = f"/api/v1/users/{create_valid_user.pk}/"
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
    response = user_client.post(
        "/api/v1/users/",
        {"email": "email@mail.com"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_userprofile_error_response(create_valid_user, user_client):
    """
    Ensure we get error 404 while trying to connect to non-exist user profile url.
    """
    url = f"/api/v1/users/{create_valid_user.pk}/profile/"
    response = user_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_user_profile_list_response(user_with_profile, user_client):
    """
    Ensure we can connect to user profile list url.
    """
    user_with_profile(group="IPZ-41")
    endpoint = "/api/v1/users/profiles/"
    response = user_client.get(endpoint)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_group_list_response(user_with_profile, user_client):
    """
    Ensure response contains only users of the required group.
    """

    profile = user_with_profile(group="IPZ-41")
    endpoint = f"/api/v1/users/group/{profile.group}/"
    response = user_client.get(endpoint)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_groups_list_response(user_with_profile, user_client):
    """
    Ensure we can connect to user groups list url.
    """
    user_with_profile(group="IPZ-41")
    user_with_profile(group="IPZ-31")
    endpoint = "/api/v1/users/groups/"
    response = user_client.get(endpoint)

    assert response.status_code == status.HTTP_200_OK
