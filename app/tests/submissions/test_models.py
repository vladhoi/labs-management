import pytest
import os
from submissions.models import Submission
from django.db.utils import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_create_submission(create_valid_user, create_valid_assigment, lab_path):
    """
    Ensure we can create a new submission.
    """
    file = SimpleUploadedFile("labtest.txt", b"these are the contents of the txt file")
    submission = Submission.objects.create(
        feedback="Test test test",
        attached_file=file,
        assigment=create_valid_assigment,
        created_by=create_valid_user,
    )

    assert submission.feedback == "Test test test"
    assert submission.created_by.email == "example@mail.com"

    # Delete file after testing
    os.remove(f"{lab_path}/{file.name}")


@pytest.mark.django_db
def test_create_submission_without_assigment(create_valid_user, lab_path):
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
    # Delete file after testing
    os.remove(f"{lab_path}/{file.name}")


@pytest.mark.django_db
def test_create_submission_without_user(create_valid_assigment, lab_path):
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
    # Delete file after testing
    os.remove(f"{lab_path}/{file.name}")
