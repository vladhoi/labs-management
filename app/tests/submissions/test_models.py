import pytest
from submissions.models import Submission
from django.db.utils import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


@pytest.mark.django_db
def test_create_submission(create_valid_user, create_valid_assigment, tmpdir):
    """
    Ensure we can create a new submission.
    """
    settings.MEDIA_ROOT = tmpdir.mkdir("test")
    file = SimpleUploadedFile("labtest.txt", b"these are the contents of the txt file")
    submission = Submission.objects.create(
        feedback="Test test test",
        attached_file=file,
        assigment=create_valid_assigment,
        created_by=create_valid_user,
    )

    assert submission.feedback == "Test test test"
    assert submission.created_by.email == "example@mail.com"


@pytest.mark.django_db
def test_create_submission_without_assigment(create_valid_user):
    """
    Ensure we can't create a new submission without a assigment.
    """
    file = SimpleUploadedFile("labtest.txt", b"these are the contents of the txt file")
    with pytest.raises(IntegrityError):
        Submission.objects.create(
            feedback="Test test test",
            attached_file=file,
            assigment=None,
            created_by=create_valid_user,
        )


@pytest.mark.django_db
def test_create_submission_without_user(create_valid_assigment):
    """
    Ensure we can't create a new submission without a user.
    """
    file = SimpleUploadedFile("labtest.txt", b"these are the contents of the txt file")
    with pytest.raises(IntegrityError):
        Submission.objects.create(
            feedback="Test test test",
            attached_file=file,
            assigment=create_valid_assigment,
            created_by=None,
        )
