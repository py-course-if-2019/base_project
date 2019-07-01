import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from celery import shared_task
from .processor import process_image
from .models import Image


@shared_task
def add(x, y):
    time.sleep(10)
    return x + y


@shared_task
def process(image_id):
    print('Call image processing')
    process_image(image_id)


@receiver(post_save, sender=Image)
def save_image(sender, instance, **kwargs):
    if not instance.resize_image:
        process.delay(instance.pk)
