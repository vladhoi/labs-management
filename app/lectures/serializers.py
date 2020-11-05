from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = "__all__"

        validators = [
            UniqueTogetherValidator(
                queryset=Lecture.objects.all(),
                fields=["title", "user"],
                message="Lecture with this title and user already exists",
            )
        ]

    def create(self, validated_data):
        return Lecture.objects.create(**validated_data)
