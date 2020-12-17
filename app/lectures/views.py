# Create your views here.
from rest_framework import viewsets
from .models import Lecture
from .serializers import LectureSerializer


class LectureViewList(viewsets.ModelViewSet):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
