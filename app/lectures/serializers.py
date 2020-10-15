from rest_framework import serializers

from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = "__all__"

    def create(self, validated_data):
        return Lecture.objects.create(**validated_data)
