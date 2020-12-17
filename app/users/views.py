from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserSerializer,
    NewUserSerializer,
    UserProfileSerializer,
    UserGroupSerializer,
)
from .models import User, UserProfile
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView


@permission_classes([IsAuthenticated])
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return NewUserSerializer
        return UserSerializer


@permission_classes([IsAuthenticated])
class UserProfileView(APIView):
    def get(self, request, pk):
        profile = get_object_or_404(UserProfile, user=pk)
        serializer = UserProfileSerializer(profile)

        return Response(serializer.data)

    def post(self, request, pk):
        profile = UserProfile(**request.data)
        profile.user = get_user_model().objects.get(pk=pk)
        profile.save()

        return Response("Success")


@permission_classes([IsAuthenticated])
class UserProfileList(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserProfileSerializer(queryset, many=True)

        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class GroupUserListView(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        group = kwargs.get("group", "")
        queryset = UserProfile.objects.filter(group=group)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class UserGroupList(ListAPIView):
    queryset = UserProfile.objects.distinct("group").only("group")
    serializer_class = UserGroupSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserGroupSerializer(queryset, many=True)

        return Response(serializer.data)
