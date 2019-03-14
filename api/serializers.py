from rest_framework import serializers

from .models import Question, Answers


# class VoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vote
#         fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    #votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Answers
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    Answers = AnswerSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = '__all__'