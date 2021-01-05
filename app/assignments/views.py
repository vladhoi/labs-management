from rest_framework import viewsets

from .models import Assignment
from .serializers import AssignmentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from submissions.models import Submission
from submissions.serializers import SubmissionSerializer


class AssignmentViewList(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()


class UserAssignmentsViewList(ListAPIView):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id", "")
        queryset = Assignment.objects.filter(created_by=user_id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class AssignmentSubmissionsViewList(ListAPIView):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        assignment_id = kwargs.get("id", "")
        queryset = Submission.objects.filter(assignment=assignment_id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
