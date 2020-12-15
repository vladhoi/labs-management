import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
@pytest.mark.parametrize("url", [reverse("subjects-list")])
def test_subject_list_response(url, user_client):
    """
    Ensure we can connect to subjects list url.
    """
    assert user_client.get(url).status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_subject_success(create_valid_user, user_client):
    """
    Ensure we can add new subject.
    """
    response = user_client.post(
        "/api/v1/subjects/",
        {"title": "test", "description": "test test test"},
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_subject_error_response(user_client):
    """
    Ensure we get error 404 while trying to connect to non-exist subject url.
    """
    response = user_client.get("/api/v1/subjects/1/get-404")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_post_subject_failure(create_valid_user, user_client):
    """
    Ensure we can add new subject.
    """
    response = user_client.post(
        "/api/v1/subjects/",
        {"title": "", "description": "test test test"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_post_uniqueness(create_valid_user, user_client):
    """
    Ensure we can't add equal subject.
    """
    response = user_client.post(
        "/api/v1/subjects/",
        {
            "title": "Python core",
            "description": "Introduction to python",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED

    response = user_client.post(
        "/api/v1/subjects/",
        {
            "title": "Python core",
            "description": "Introduction to python",
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
