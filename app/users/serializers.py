from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    pass
