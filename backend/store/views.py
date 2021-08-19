from datetime import datetime

from django.db.models import query
from rest_framework import generics, views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetailView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileUploadView(views.APIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None, *args, **kwargs):
        file_obj = request.data['file']
        file_obj.name = f'{datetime.now()}-{filename}'

        file = File(filename=file_obj)
        file.save()

        serializer = FileSerializer(file)
        return Response(serializer.data, status=201)
