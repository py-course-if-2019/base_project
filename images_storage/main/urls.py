from django.urls import path
from . import views
from .processor import processed


urlpatterns = [
    path('', views.main, name='main'),
    path('images/', views.ImageListView.as_view(), name='images')
    # path('images/', processed(4), name='images')      #my debag
]
