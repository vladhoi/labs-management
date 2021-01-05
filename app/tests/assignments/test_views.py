import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
@pytest.mark.parametrize("url", [reverse("assignments-list")])
def test_assignment_list_response(url, user_client):
    """
    Ensure we can connect to assignments list url.
    """
    assert user_client.get(url).status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_assignment_success(create_valid_user, user_client):
    """
    Ensure we can add new assignment.
    """
    user = create_valid_user
    response = user_client.post(
        "/api/v1/assignments/",
        {"title": "test", "description": "test test test", "created_by": user.pk},
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_assignment_error_response(user_client):
    """
    Ensure we get error 404 while trying to connect to non-exist assignment url.
    """
    response = user_client.get("/api/v1/assignments/1/get-404")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_post_assignment_failure(create_valid_user, user_client):
    """
    Ensure we can add new assignment.
    """
    user = create_valid_user
    response = user_client.post(
        "/api/v1/assignments/",
        {"title": "", "description": "test test test", "created_by": user.pk},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_user_assignment(create_valid_assignment, user_client):
    """
    Ensure we can get users assignments
    """
    url = "/api/v1/assignments/user/1/"
    response = user_client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_assignment_submissions(
    create_valid_assignment, create_valid_submission, user_client
):
    """
    Ensure we can get submissions for one assignment
    """
    url = "/api/v1/assignments/1/submissions"
    response = user_client.get(url)

    assert response.status_code == status.HTTP_200_OK
