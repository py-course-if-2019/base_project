from importlib.resources import Package

from django.http import request
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Image
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def main(request):
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

