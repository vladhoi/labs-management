from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile
from subjects.serializers import UserSubjectSerializer


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "is_staff", "is_student")
        ref_name = "Custom User serializer"


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    subjects = UserSubjectSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ("user", "first_name", "last_name", "group", "subjects")
        depth = 1


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("group",)
