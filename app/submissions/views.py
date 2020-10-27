from rest_framework import viewsets

from .models import Submission
from .serializers import SubmissionSerializer


class SubmissionViewList(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
