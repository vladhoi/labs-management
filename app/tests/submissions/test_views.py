import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
@pytest.mark.parametrize("url", [reverse("submissions-list")])
def test_submission_list_response(url, user_client):
    """
    Ensure we can connect to submission list url.
    """
    assert user_client.get(url).status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_submission_success(
    create_valid_user, create_valid_assignment, user_client
):
    """
    Ensure we can add new submission.
    """
    attached_file = SimpleUploadedFile(
        "labtest.txt", b"these are the contents of the txt file"
    )
    assignment = create_valid_assignment
    created_by = create_valid_user
    response = user_client.post(
        "/api/v1/submissions/",
        {
            "feedback": "Test test test",
            "attached_file": attached_file,
            "assignment": assignment.pk,
            "created_by": created_by.pk,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_submission_error_response(user_client):
    """
    Ensure we get error 404 while trying to connect to non-exist submission url.
    """
    response = user_client.get("/api/v1/submission/1/get-404")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_post_submission_failure(
    create_valid_user, create_valid_assignment, user_client
):
    """
    Ensure we can add new submission.
    """
    attached_file = ""
    assignment = create_valid_assignment
    created_by = create_valid_user
    response = user_client.post(
        "/api/v1/submissions/",
        {
            "feedback": "Test test test",
            "attached_file": attached_file,
            "assignment": assignment.pk,
            "created_by": created_by.pk,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
