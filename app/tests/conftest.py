import pytest
from django.db import connection
from django.db.models.base import ModelBase
from lectures.models import Lecture
from subjects.models import Subject
from submissions.models import Submission
from users.models import User, UserProfile
from assignments.models import Assignment
from django.test import override_settings
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile

from utils.models import AbstractTableMeta


@pytest.fixture()
def create_valid_user():
    """
    Make fixture that returns valid user.
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
    Make fixtures that returns invalid user.
    """
    return request.param


@pytest.fixture()
def create_valid_subject(create_valid_user):
    """
    Make fixture that returns valid subject.
    """
    data = {
        "title": "Subject_1",
        "description": "Description",
    }
    return Subject.objects.create(**data)


@pytest.fixture()
def create_valid_lecture(create_valid_user, create_valid_subject):
    """
    Make fixture that returns valid lecture.
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
def create_valid_assignment(create_valid_user):
    """
    Make fixture that returns valid assigment
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


@pytest.fixture()
def create_second_valid_subject(create_valid_user):
    """
    Make fixture that returns valid subject.
    """
    data = {
        "created_by": create_valid_user,
        "title": "Subject_2",
        "description": "Description",
    }
    return Subject.objects.create(**data)


@pytest.fixture()
def create_valid_submission(create_valid_user, create_valid_assignment):
    """
    Make fixture that returns valid submission
    """
    data = {
        "feedback": "Test test test",
        "attached_file": SimpleUploadedFile(
            "labtest.txt", b"these are the contents of the txt file"
        ),
        "assignment": create_valid_assignment,
        "created_by": create_valid_user,
    }
    return Submission.objects.create(**data)


@pytest.fixture()
def create_second_valid_submission(create_valid_user, create_valid_assignment):
    """
    Make fixture that returns valid submission
    """
    data = {
        "feedback": "Second test",
        "attached_file": SimpleUploadedFile(
            "labtest.txt", b"these are the contents of the another txt file"
        ),
        "assignment": create_valid_assignment,
        "created_by": create_valid_user,
    }
    return Submission.objects.create(**data)


@pytest.fixture()
def create_second_valid_assignment(create_valid_user):
    """
    Make fixture that returns valid assignment
    """
    data = {
        "title": "Second Test",
        "description": "Test test test",
        "created_by": create_valid_user,
    }
    return Assignment.objects.create(**data)


@pytest.fixture()
@pytest.mark.django_db
def dummy_model():
    """
    Fixture for dummy model, which inherits AbstractTableMeta
    """

    mixin = AbstractTableMeta

    DummyModel = ModelBase(
        mixin.__name__,
        (mixin,),
        {"__module__": mixin.__module__},
    )

    with connection.schema_editor() as se:
        se.create_model(DummyModel)

    yield DummyModel

    with connection.schema_editor() as schema_editor:
        schema_editor.delete_model(DummyModel)


@pytest.fixture()
def user_with_profile(create_valid_user):
    """
    Make fixture that return valid assignment
    """

    def __instance(**kwargs):
        data = {
            "user": create_valid_user,
            "first_name": "test",
            "last_name": "test",
            "group": "",
        }
        data.update(kwargs)
        user_profile = UserProfile(**data)
        return user_profile

    return __instance
