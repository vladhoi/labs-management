from rest_framework import viewsets
from rest_framework import generics
from .models import Submission
from .serializers import SubmissionSerializer
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.shortcuts import get_object_or_404


class SubmissionViewList(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()


class FileDownloadAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        filename = kwargs.get("filename", "")
        queryset = get_object_or_404(Submission, attached_file__contains=filename)
        document = queryset.attached_file.open()
        response = HttpResponse(
            FileWrapper(document), content_type="application/msword"
        )
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response
