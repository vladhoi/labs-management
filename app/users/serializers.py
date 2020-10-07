from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())

    class Meta:
        model = UserProfile
        fields = ('__all__')
