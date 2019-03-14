from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Question, Answers
from  .serializers import QuestionSerializer,AnswerSerializer

class Questionlist(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Question, pk=pk)
        data = QuestionSerializer(poll).data
        return Response(data)

class Answerlist(generics.ListCreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


# class CreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer