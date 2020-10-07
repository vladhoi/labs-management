import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import UserProfile, User


def test_create_account():
    """
    Ensure we can create a new account object.
    """
    client = APIClient()
    url = reverse('users')
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
