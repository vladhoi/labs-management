import pytest
from datetime import date
from lectures.models import Lecture
from subjects.models import Subject
from users.models import User
from assignments.models import Assignment
from django.conf import settings


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


@pytest.fixture
def lab_path():
    today = date.today()
    LABS_PATH = f"labs/{today.year}/{today.month}/{today.day}"
    return f"{settings.MEDIA_ROOT}/{LABS_PATH}/"
