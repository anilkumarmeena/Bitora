from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Questions
from .serializers import queSerializer



class Listque(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = queSerializer

    def post(self, request):
        # Create an article from the above data
        serializer = queSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "'{}' created successfully".format(article_saved.title)})