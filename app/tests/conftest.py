import pytest
from subjects.models import Subject
from users.models import User


@pytest.fixture()
def create_valid_user():
    """
    Make fixture that return valid user.
    """
    data = {"email": "example@mail.com", "password": "S_t_r_o_n_g"}
    return User.objects.create_user(**data)


@pytest.fixture(
    params=[
        {"email": "mail", "password": "pass1234"},
        {"email": "example@mail.com", "password": "1234567"},
        {"email": "example@mail.com", "password": "abcdefgh"},
        {"email": "example@mail.com", "password": "pass"},
    ]
)
def invalid_user_data(request):
    """
    Make fixtures that return invalid user.
    """
    return request.param


@pytest.fixture()
def create_valid_subject(create_valid_user):
    """
    Make fixture that return valid subject.
    """
    data = {
        "title": "Subject_1",
        "description": "Description",
        "user": create_valid_user,
    }
    return Subject.objects.create(**data)
