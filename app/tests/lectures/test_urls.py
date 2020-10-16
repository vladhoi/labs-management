import pytest
from django.test import Client
from rest_framework.reverse import reverse


@pytest.mark.django_db
@pytest.mark.parametrize("url", [reverse("lecture-list-list")])
def test_lecture_list_response(url):
    """
    Ensure we can connect to lecture list url
    """
    client = Client()
    assert 200 == client.get(url).status_code


@pytest.mark.django_db
def test_lecture_error_response():
    """
    Ensure we get error 404 while trying to connect to non-exist lecture url
    """
    client = Client()
    response = client.get("/api/v1/lectures/1/get-404")
    assert 404 == response.status_code
