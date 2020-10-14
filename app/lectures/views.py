# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lecture
from .serializers import LectureSerializer


class LectureView(APIView):
    def get(self, request, pk):
        profile = Lecture.objects.get(user=pk)
        serializer = LectureSerializer(profile)
        return Response(serializer.data)
