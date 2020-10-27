import pytest
from subjects.models import Subject
from subjects.serializers import SubjectSerializer
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_all_subjects(
    create_valid_subject, create_second_valid_subject, user_client
):
    """
    Ensure we get all subject in proper format.
    """
    create_valid_subject
    create_second_valid_subject
    response = user_client.get(reverse("subjects-list"))
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_get_single_subject(create_valid_subject, user_client):
    """
    Ensure we get single subject in proper format.
    """
    sub = create_valid_subject
    response = user_client.get(f"/api/v1/subjects/{sub.pk}/")
    subject = Subject.objects.get(title="Subject_1")
    serializer = SubjectSerializer(subject)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_handle_non_existed_lecture_properly(user_client):
    """
    Ensure we get non-existed subject in proper format.
    """
    response = user_client.get("/api/v1/subjects/999/")
    assert response.data == {"detail": "Not found."}
