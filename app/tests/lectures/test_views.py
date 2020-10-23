import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
@pytest.mark.parametrize("url", [reverse("lecture-list-list")])
def test_lecture_list_response(url, user_client):
    """
    Ensure we can connect to lecture list url.
    """
    response = user_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_lecture_error_response(user_client):
    """
    Ensure we get error 404 while trying to connect to non-exist lecture url.
    """
    response = user_client.get("/api/v1/lectures/1/get-404")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_post_lecture_success(create_valid_user, create_valid_subject, user_client):
    """
    Ensure we can add new lecture.
    """
    user = create_valid_user
    subject = create_valid_subject
    response = user_client.post(
        "/api/v1/lectures/",
        {"title": "Title", "text": "Text", "user": user.pk, "subject": subject.pk},
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_lecture_failure(create_valid_user, create_valid_subject, user_client):
    """
    Ensure we can't add new lecture.
    """
    user = create_valid_user
    subject = create_valid_subject
    response = user_client.post(
        "/api/v1/lectures/",
        {"title": "", "text": "Text", "user": user.pk, "subject": subject.pk},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
