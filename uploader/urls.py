from django.urls import path
from .views import FileUploadView, FileBrowserView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('file_browser/', FileBrowserView.as_view(), name='file_browser'),
]