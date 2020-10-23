import pytest
from lectures.models import Lecture
from lectures.serializers import LectureSerializer
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_all_lectures(
    create_valid_lecture, create_second_valid_lecture, user_client, user
):
    """
    Ensure we get all lectures in proper format.
    """
    response = user_client.get(reverse("lecture-list-list"))
    lectures = Lecture.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_get_single_lecture(create_valid_lecture, user_client, user):
    """
    Ensure we get single lecture in proper format.
    """
    lec = create_valid_lecture
    response = user_client.get(f"/api/v1/lectures/{lec.pk}/")
    lecture = Lecture.objects.get(title="Lecture_1")
    serializer = LectureSerializer(lecture)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_handle_non_existed_lecture_properly(user_client):
    """
    Ensure we get non-existed lecture in proper format.
    """
    response = user_client.get("/api/v1/lectures/999/")
    assert response.data == {"detail": "Not found."}
