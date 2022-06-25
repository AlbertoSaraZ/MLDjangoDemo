from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .forms import MemeUploadForm, SearchMemeForm
from .models import CNNImage


class ImageUploadView(FormView):
    template_name = 'meme_upload.html'
    form_class = MemeUploadForm
    success_url = 'single_meme'

    def get_success_url(self, **kwargs):
        return reverse_lazy('single_meme', kwargs={'pk': self.pk})

    def form_valid(self, form):
        item = form.save()

        # Saves item pk to send user to detail view of the image that was just uploaded

        self.pk = item.pk
        return super(ImageUploadView, self).form_valid(form)


class MemeGallery(FormMixin, ListView):
    template_name = 'gallery.html'
    model = CNNImage
    paginate_by = 5
    queryset = CNNImage.objects.order_by('-id')
    form_class = SearchMemeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        context['query'] = query
        for image in context['object_list']:
            image.meme_confidence = image.meme_confidence * 100
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(request_data=self.request)
        return kwargs

    def get(self, *args, **kwargs):
        form_class = self.get_form_class()
        search_form = self.get_form(form_class)
        query = self.request.GET.get('search')

        if query:
            self.object_list = self.get_queryset().filter(name__contains=query)
        else:
            self.object_list = self.get_queryset()

        # Search form is passed and kwargs updated to keep query in input field in form

        context = self.get_context_data(object_list=self.object_list, form=search_form)
        return self.render_to_response(context)


class SingleMeme(DetailView):
    template_name = 'single_meme.html'
    model = CNNImage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # meme_confidence is stored as a float from 0 to 1, it's better to change here than in template
        context['object'].meme_confidence = context['object'].meme_confidence * 100
        return context


class DeleteMeme(DeleteView):
    template_name = "confirm_delete.html"
    model = CNNImage
    success_url = reverse_lazy('gallery')
