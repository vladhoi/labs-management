from rest_framework import serializers
from subjects.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "title", "description"]

    def create(self, validated_data):
        """
        Create and return a new `Subject` instance, given the validated data.
        """
        return Subject.objects.create(**validated_data)
