import pytest
from submissions.models import Submission
from submissions.serializers import SubmissionSerializer
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_all_submissions(
    create_valid_submission, create_second_valid_submission, user_client
):
    """
    Ensure we get all submissions in proper format.
    """
    create_valid_submission
    create_second_valid_submission
    response = user_client.get(reverse("submissions-list"))
    submissions = Submission.objects.all()
    serializer = SubmissionSerializer(submissions, many=True)
    serializer_copy = serializer.data
    for submission in serializer_copy:
        submission["attached_file"] = "http://testserver" + submission["attached_file"]
    assert response.data == serializer_copy


@pytest.mark.django_db
def test_get_single_submission(create_valid_submission, user_client):
    """
    Ensure we get single submission in proper format.
    """
    submit = create_valid_submission
    response = user_client.get(f"/api/v1/submissions/{submit.pk}/")
    submission = Submission.objects.get(feedback="Test test test")
    serializer = SubmissionSerializer(submission)
    serializer_copy = serializer.data
    serializer_copy["attached_file"] = (
        "http://testserver" + serializer_copy["attached_file"]
    )
    assert response.data == serializer_copy


@pytest.mark.django_db
def test_handle_non_existed_submission_properly(user_client):
    """
    Ensure we get non-existed submission in proper format.
    """
    response = user_client.get("/api/v1/submissions/999/")
    assert response.data == {"detail": "Not found."}
