from rest_framework import generics
from .models import Questions
from .serializers import queSerializer


class Listque(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = queSerializer