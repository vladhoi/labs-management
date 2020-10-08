from rest_framework.views import APIView
from rest_framework import generics
from .serializers import SubjectSerializer
from .models import Subject


class SubjectList(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer