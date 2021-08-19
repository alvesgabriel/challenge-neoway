from django.urls import path, re_path

from .views import (
    FileDetailView,
    FileListView,
    FileUploadView,
    SaleDetailView,
    SaleListView,
)

app_name = "store"
urlpatterns = [
    path("files/", FileListView.as_view()),
    path("files/<int:pk>/", FileDetailView.as_view()),
    re_path(r"files/(?P<filename>upload)/", FileUploadView.as_view()),
    path("sales/", SaleListView.as_view()),
    path("sales/<int:pk>/", SaleDetailView.as_view()),
]
