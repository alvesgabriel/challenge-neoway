import uuid

from rest_framework import generics, views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .models import File, Sale
from .serializers import FileSerializer, SaleSerializer
from .utils import parse_file


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
        file_obj = request.data["file"]
        file_obj.name = f"{uuid.uuid4().hex}.txt"
        lines = file_obj.readlines()

        file = File(filename=file_obj)
        file.save()

        sales = [Sale(**sale) for sale in parse_file(lines, file)]
        Sale.objects.bulk_create(sales)

        serializer = FileSerializer(file)
        return Response(serializer.data, status=201)


class SaleListView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetailView(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
