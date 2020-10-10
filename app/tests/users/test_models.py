import pytest
from django.core.exceptions import ValidationError
from users.models import User


@pytest.fixture()
def create_valid_user():
    data = {
        "email": "example@mail.com",
        "password": "S_t_r_o_n_g"
    }
    return User.objects.create_user(**data)


@pytest.fixture(params=[
    {
        "email": "mail",
        "password": "pass1234"
    },
    {
        "email": "example@mail.com",
        "password": "1234567"
    },
    {
        "email": "example@mail.com",
        "password": "abcdefgh"
    },
    {
        "email": "example@mail.com",
        "password": "pass"
    }
])
def invalid_user_data(request):
    return request.param


@pytest.mark.django_db
def test_create_user(create_valid_user):
    """
    Ensure we can create a new user object.
    """
    u = create_valid_user
    assert User.objects.count() == 1
    assert u.email == "example@mail.com"


@pytest.mark.django_db
def test_delete_user(create_valid_user):
    """
    Ensure we can delete a user object.
    """
    u = create_valid_user
    res = User.objects.filter(pk=u.pk).delete()
    assert res[0] == 1


@pytest.mark.django_db
@pytest.mark.xfail(raises=ValidationError)
def test_create_user_fail(invalid_user_data):
    """
    Ensure we can't create a new user object with invalid data (email and password).
    """
    u = User.objects.create_user(**invalid_user_data)


@pytest.mark.django_db
@pytest.mark.uniq
def test_uniqueness_user(create_valid_user):
    """
    Ensure we can't create the same user object.
    """
