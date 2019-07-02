from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Image
from django.forms import ModelForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect

from .tasks import add
from .models import Image


def main(request):
    return render(request, 'main/index.html')


class ImageUploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ['original_image']


class ImageUploadView(View):

    model = Image

    def post(self, request, *args, **kwargs):
        if self.request.FILES:
            for f in self.request.FILES.getlist('files'):
                obj = self.model.objects.create(original_image=f)
        # return render(request, 'main/index.html')
        return redirect('images')

    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html')

class ImageListView(ListView):
    model = Image
    template_name = "main/image_list.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ImageListView, self).get_context_data(**kwargs)
        image_list = Image.objects.all()
        paginator = Paginator(image_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            image_list = paginator.page(page)
        except PageNotAnInteger:
            image_list = paginator.page(1)
        except EmptyPage:
            image_list = paginator.page(paginator.num_pages)

        context['image_list'] = image_list
        return context


def test(request):
    add.delay(1, 2)
    return render(request, 'main/index.html')

