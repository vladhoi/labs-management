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
    )

    assert subject.title == "Test"
    assert subject.description == "Test test test"


@pytest.mark.django_db
def test_create_subject_without_title(create_valid_user):
    """
    Ensure we can't create a new subject without a user.
    """
    with pytest.raises(IntegrityError):
        Subject.objects.create(
            title=None,
            description="Test test test",
        )


@pytest.mark.django_db
@pytest.mark.xfail(raises=IntegrityError)
def test_create_two_equal_subject(create_valid_subject):
    """
    Ensure we can't create two equal subject.
    """
    create_valid_subject.save()
    create_valid_subject.save()

    assert Subject.objects.count() == 1
