# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Lecture
from .serializers import LectureSerializer


class LectureViewList(viewsets.ViewSet):
    def list(self, request):
        queryset = Lecture.objects.all()
        serializer = LectureSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Lecture.objects.all()
        lecture = get_object_or_404(queryset, pk=pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)


class LectureView(CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    # def post(self, request, pk):
    #     lecture = request.data.get('lecture')

    # serializer = LectureSerializer(data=lecture)
