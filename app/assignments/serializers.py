from rest_framework import serializers
from .models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new `Assignment` instance, given the validated data.
        """
        return Assignment.objects.create(**validated_data)
