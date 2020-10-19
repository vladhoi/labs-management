from django.conf import settings
import pytest
from rest_framework import status


def test_settings():

    assert hasattr(
        settings, "REST_FRAMEWORK"
    ), "REST_FRAMEWORK configuration is not found in settings.py"

    assert "DEFAULT_AUTHENTICATION_CLASSES" in settings.REST_FRAMEWORK
    assert "DEFAULT_PERMISSION_CLASSES" in settings.REST_FRAMEWORK


@pytest.mark.django_db(transaction=True)
def test_register(user_client, user, create_valid_user):

    response = user_client.post(
        "/api/v1/users/", data={"email": "example@gmail.com", "password": "test12345"}
    )

    assert (
        response.status_code != status.HTTP_404_NOT_FOUND
    ), "Endpoint `/api/v1/users/` is not found"

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db(transaction=True)
@pytest.mark.login
def test_login(user_client, user):
    response = user_client.post(
        "/api/v1/auth/token/login",
        data={"email": "justates@gmail.com", "password": "1234567test"},
    )
    auth_data = response.data

    assert "auth_token" in auth_data
