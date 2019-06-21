from django.db import models

# Create your models here.


class Image(models.Model):
    original_image = models.ImageField()
    resize_image = models.ImageField(null=True, default=None)
    meta = models.TextField(default=None, null=True)
