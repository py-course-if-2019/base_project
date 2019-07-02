from PIL import Image as Im
from .models import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile



def process_image(image_id, scale=50):

    try:
        original = Image.objects.get(pk=image_id)
        path_in = original.original_image.path
        print(path_in)

        img_io = io.BytesIO()
        original_image = Im.open(path_in)

        original_size = (original_image.width, original_image.height)

        size = (int(original_size[0] * (scale / 100)), int(original_size[1] * (scale / 100)))

        saved, file_name = original.original_image.name.split('/')
        name, ext = file_name.split('.')

        new_size = original_image.convert('RGB').resize(size)
        new_size.save(img_io, 'jpeg')

        image_file = InMemoryUploadedFile(img_io, None, f'{name}_{size[0]}_{size[1]}.jpeg', 'image/jpeg',
                                          img_io.tell, None)
        original.resize_image.save(f'{name}_{size[0]}_{size[1]}.jpeg', image_file)

        original.save()

    except FileNotFoundError as e:
        print(repr(e))



