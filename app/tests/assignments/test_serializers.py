import pytest
from assignments.models import Assignment
from assignments.serializers import AssignmentSerializer
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_all_assignment(
    create_valid_assignment, create_second_valid_assignment, user_client
):
    """
    Ensure we get all assignments in proper format.
    """
    create_valid_assignment
    create_second_valid_assignment
    response = user_client.get(reverse("assignments-list"))
    assignments = Assignment.objects.all()
    serializer = AssignmentSerializer(assignments, many=True)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_get_single_assignment(create_valid_assignment, user_client):
    """
    Ensure we get single assignment in proper format.
    """
    asign = create_valid_assignment
    response = user_client.get(f"/api/v1/assignments/{asign.pk}/")
    assignment = Assignment.objects.get(title="Test")
    serializer = AssignmentSerializer(assignment)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_handle_non_existed_assignment_properly(user_client):
    """
    Ensure we get non-existed assignment in proper format.
    """
    response = user_client.get("/api/v1/assignments/999/")
    assert response.data == {"detail": "Not found."}
