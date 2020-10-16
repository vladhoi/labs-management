import pytest
from django.db import IntegrityError
from django.test import Client
from lectures.models import Lecture
from lectures.serializers import LectureSerializer
from rest_framework.reverse import reverse


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
def test_get_all_lectures(create_valid_lecture, create_second_valid_lecture):
    """
    Ensure we get all lectures in proper format.
    """
    create_valid_lecture
    create_second_valid_lecture
    client = Client()
    response = client.get(reverse("lecture-list-list"))
    lectures = Lecture.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_get_single_lecture(create_valid_lecture):
    """
    Ensure we get single lecture in proper format.
    """
    lec = create_valid_lecture
    client = Client()
    response = client.get(f"/api/v1/lectures/{lec.pk}/")
    lecture = Lecture.objects.get(title="Lecture_1")
    serializer = LectureSerializer(lecture)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_handle_non_existed_lecture_properly():
    client = Client()
    response = client.get("/api/v1/lectures/999/")
    assert response.data == {"detail": "Not found."}
