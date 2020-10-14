from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import UserSerializer, UserProfileSerializer
from .models import User, UserProfile


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #    raise PermissionDenied()


class UserProfileView(APIView):
    def get(self, request, pk):
        profile = UserProfile.objects.get(user=pk)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk):
        profile = UserProfile(**request.data)
        profile.user = get_user_model().objects.get(pk=pk)
        profile.save()

        return Response("Success")
