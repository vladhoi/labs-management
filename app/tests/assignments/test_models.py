import pytest
from assignments.models import Assignment
from django.db.utils import IntegrityError


@pytest.mark.django_db
def test_create_assignment(create_valid_user):
    """
    Ensure we can create a new assignment.
    """
    assignment = Assignment.objects.create(
        title="Test", description="Test test test", created_by=create_valid_user
    )

    assert assignment.title == "Test"
    assert assignment.description == "Test test test"
    assert assignment.created_by.email == "example@mail.com"


@pytest.mark.django_db
def test_create_assignment_without_user():
    """
    Ensure we can't create a new assignment without a user.
    """
    with pytest.raises(IntegrityError):
        Assignment.objects.create(
            title="Test", description="Test test test", created_by=None
        )
