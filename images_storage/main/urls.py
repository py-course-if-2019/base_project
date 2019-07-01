from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('images/', views.ImageListView.as_view(), name='images'),
    path('test/', views.test, name='test'),
    path('upload/', views.ImageUploadView.as_view(), name='upload')
]
