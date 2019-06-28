from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Image


def main(request):
    return render(request, 'main/index.html')


class ImageListView(ListView):
    queryset = Image.objects.all()
    template_name = 'main/image_list.html'
