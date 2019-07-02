from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    original_image = models.ImageField(upload_to='original')
    resize_image = models.ImageField(null=True, default=None, blank=True, upload_to='processed')
    meta = models.TextField(default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Image'
