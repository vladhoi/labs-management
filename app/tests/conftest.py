import pytest
from lectures.models import Lecture
from subjects.models import Subject
from users.models import User
from assignments.models import Assignment
from django.test import override_settings
from rest_framework.test import APIClient


@pytest.fixture()
def create_valid_user():
    """
    Make fixture that return valid user.
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
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


@pytest.fixture()
def create_valid_lecture(create_valid_user, create_valid_subject):
    """
    Make fixture that return valid lecture.
    """
    data = {
        "title": "Lecture_1",
        "text": "Text_1",
        "user": create_valid_user,
        "subject": create_valid_subject,
    }

    return Lecture.objects.create(**data)


@pytest.fixture()
def create_second_valid_lecture(create_valid_user, create_valid_subject):
    """
    Make fixture that return valid lecture.
    """
    data = {
        "title": "Lecture_2",
        "text": "Text_2",
        "user": create_valid_user,
        "subject": create_valid_subject,
    }

    return Lecture.objects.create(**data)


@pytest.fixture()
def create_valid_assigment(create_valid_user):
    """
    Make fixture that return valid assigment
    """
    data = {
        "title": "Test",
        "description": "Test test test",
        "created_by": create_valid_user,
    }
    return Assignment.objects.create(**data)


@pytest.fixture(scope="session", autouse=True)
def custom_media_root(tmpdir_factory):
    overrided_media_root = override_settings(
        MEDIA_ROOT=str(tmpdir_factory.mktemp("test_media"))
    )
    overrided_media_root.enable()


@pytest.fixture
def token(user):
    from rest_framework.authtoken.models import Token

    token, _ = Token.objects.get_or_create(user=user)
    return token.key


@pytest.fixture
def user_client(token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    return client


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        email="justates@gmail.com", password="1234567test"
    )
