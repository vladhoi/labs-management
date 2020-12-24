from rest_framework import serializers
from subjects.models import Subject
from rest_framework.validators import UniqueTogetherValidator


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "title", "description", "created_by")

        validators = [
            UniqueTogetherValidator(
                queryset=Subject.objects.all(),
                fields=["title"],
                message="Subject with this title already exists",
            )
        ]

    def create(self, validated_data):
        """
        Create and return a new `Subject` instance, given the validated data.
        """
        return Subject.objects.create(**validated_data)


class UserSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = ("users",)
