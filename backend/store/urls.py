from django.urls import path, re_path

from .views import FileDetailView, FileListView, FileUploadView

app_name = 'store'
urlpatterns = [
    path('files/', FileListView.as_view()),
    path('files/<int:pk>/', FileDetailView.as_view()),
    re_path(r'files/upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
]
