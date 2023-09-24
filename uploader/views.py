from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UploadedFile
from .forms import FileUploadForm

class FileUploadView(LoginRequiredMixin, CreateView):
    model = UploadedFile
    form_class = FileUploadForm
    template_name = 'uploader/upload.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FileBrowserView(LoginRequiredMixin, ListView):
    model = UploadedFile
    template_name = 'uploader/file_browser.html'
    context_object_name = 'files'