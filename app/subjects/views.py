from rest_framework import viewsets
from .serializers import SubjectSerializer
from .models import Subject
from lectures.models import Lecture
from lectures.serializers import LectureSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class SubjectViewList(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectLectureListView(ListAPIView):
    serializer_class = LectureSerializer

    def get_queryset(self):
        pass

    def get(self, request, pk):
        queryset = Lecture.objects.filter(subject=pk)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
