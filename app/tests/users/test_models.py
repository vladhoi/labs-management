import pytest

from users.models import BasicUser


@pytest.mark.django_db
def test_user_model():
    test_user = BasicUser(
        first_name="Test",
        last_name="Test",
        age="12"
    )
    test_user.save()

    assert test_user.first_name == "Test"
    assert test_user.last_name == "Test"
    assert test_user.age == "12"
    assert test_user.created_date
    assert test_user.updated_date
