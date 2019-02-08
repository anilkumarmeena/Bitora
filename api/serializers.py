from rest_framework import serializers
from .models import Questions


class queSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ("title", "content","time")

        def create(self, validated_data):
            return Questions.objects.create(**validated_data)