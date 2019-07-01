from django.db import models


class Image(models.Model):
    original_image = models.ImageField(upload_to='original')
    resize_image = models.ImageField(null=True, default=None, blank=True, upload_to='processed')
    meta = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return 'Image'
