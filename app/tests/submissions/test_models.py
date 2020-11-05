import pytest
from submissions.models import Submission
from django.db.utils import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_create_submission(create_valid_user, create_valid_assignment):
    """
    Ensure we can create a new submission.
    """
    file = SimpleUploadedFile("labtest.txt", b"these are the contents of the txt file")
    submission = Submission.objects.create(
        feedback="Test test test",
        attached_file=file,
        assignment=create_valid_assignment,
        created_by=create_valid_user,
    )

    assert submission.feedback == "Test test test"
    assert submission.created_by.email == "example@mail.com"


@pytest.mark.django_db
def test_create_submission_without_assignment(create_valid_user):
    """
    Ensure we can't create a new submission without a assignment.
    """
    file = SimpleUploadedFile("labtest.txt", b"these are the contents of the txt file")
    with pytest.raises(IntegrityError):
        Submission.objects.create(
            feedback="Test test test",
            attached_file=file,
            assignment=None,
            created_by=create_valid_user,
        )


@pytest.mark.django_db
def test_create_submission_without_user(create_valid_assignment):
    """
    Ensure we can't create a new submission without a user.
    """
    file = SimpleUploadedFile("labtest.txt", b"these are the contents of the txt file")
    with pytest.raises(IntegrityError):
        Submission.objects.create(
            feedback="Test test test",
            attached_file=file,
            assignment=create_valid_assignment,
            created_by=None,
        )


@pytest.mark.django_db
def test_delete_submission(create_valid_submission):
    """
    Ensure we can delete a submission.
    """
    submit = create_valid_submission
    res = Submission.objects.filter(pk=submit.pk).delete()
    assert res[0] == 1
