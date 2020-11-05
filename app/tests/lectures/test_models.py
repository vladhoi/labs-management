import pytest
from django.db import IntegrityError
from lectures.models import Lecture


@pytest.mark.django_db
def test_create_lecture(create_valid_subject, create_valid_user):
    """
    Ensure we can create a new lecture.
    """
    data = {
        "title": "Lecture",
        "text": "Text",
        "user": create_valid_user,
        "subject": create_valid_subject,
    }
    lec = Lecture.objects.create(**data)
    assert lec.title == "Lecture"
    assert lec.text == "Text"


@pytest.mark.django_db
@pytest.mark.xfail(raises=IntegrityError)
def test_create_lecture_without_user(create_valid_subject):
    """
    Ensure we can't create a new lecture without user.
    """
    data = {"title": "Lecture", "text": "Text", "subject": create_valid_subject}
    Lecture.objects.create(**data)


@pytest.mark.django_db
@pytest.mark.xfail(raises=IntegrityError)
def test_create_lecture_without_subject(create_valid_user):
    """
    Ensure we can't create a new lecture without subject.
    """
    data = {"title": "Lecture", "text": "Text", "user": create_valid_user}
    Lecture.objects.create(**data)


@pytest.mark.django_db
@pytest.mark.xfail(raises=IntegrityError)
def test_create_two_equal_lectures(create_valid_lecture):
    """
    Ensure we can't create two equal lectures.
    """
    create_valid_lecture.save()
    create_valid_lecture.save()

    assert Lecture.objects.count() == 1
