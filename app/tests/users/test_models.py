import pytest


@pytest.mark.django_db
def test_create_user():
    """
    Ensure we can create a new user object.
    """


@pytest.mark.django_db
@pytest.mark.xfail
def test_create_user_fail():
    """
    Ensure we can't create a new user object with unvalid data.
    """
