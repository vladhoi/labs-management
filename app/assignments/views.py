from rest_framework import viewsets

from .models import Assignment
from .serializers import AssignmentSerializer


class AssignmentViewList(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
