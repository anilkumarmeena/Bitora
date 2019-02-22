from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Entry
from .serializers import queSerializer



class Listque(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = queSerializer

    def post(self, request):
        serializer = queSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "'{}' created successfully".format(article_saved.title)})