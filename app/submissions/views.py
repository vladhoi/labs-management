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


class FileDownloadListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        folder = kwargs.get("folder", "")
        year = kwargs.get("year", "")
        month = kwargs.get("month", "")
        day = kwargs.get("day", "")
        filename = kwargs.get("filename", "")
        attached_file = f"{folder}/{year}/{month}/{day}/{filename}"
        queryset = get_object_or_404(Submission, attached_file=attached_file)
        file_handle = queryset.attached_file.open()
        document = file_handle
        response = HttpResponse(
            FileWrapper(document), content_type="application/msword"
        )
        response[
            "Content-Disposition"
        ] = f"attachment; filename={queryset.attached_file}"
        return response
