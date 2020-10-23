import pytest
from subjects.models import Subject
from django.db.utils import IntegrityError


@pytest.mark.django_db
def test_create_subject(create_valid_user):
    """
    Ensure we can create a new subject.
    """
    subject = Subject.objects.create(
        title="Test",
        description="Test test test",
        user=create_valid_user,
    )

    assert subject.title == "Test"
    assert subject.user.email == "example@mail.com"
    assert subject.description == "Test test test"


@pytest.mark.django_db
def test_create_subject_without_user():
    """
    Ensure we can't create a new subject without a user.
    """
    with pytest.raises(IntegrityError):
        Subject.objects.create(
            title="Test",
            description="Test test test",
            user=None,
        )


@pytest.mark.django_db
def test_create_subject_without_title(create_valid_user):
    """
    Ensure we can't create a new subject without a user.
    """
    with pytest.raises(IntegrityError):
        Subject.objects.create(
            title=None,
            description="Test test test",
            user=create_valid_user,
        )
