from PIL import Image as Im
import os
from .models import Image



def processed(Image_id, scale = 50):

    try:
        oll = Image.objects.all()
        original = Image.objects.get(id=Image_id)
        path_in = original.original_image
        path_out = original.resize_image
        original_temp_image = Im.open(path_in)

        original_size = (original_temp_image.width, original_temp_image.height)
        size = (int(original_size[0] * (scale / 100)),int(original_size[1] * (scale / 100)))
        # saved, ext = os.path.splitext(path_out)

        new_size = original_temp_image.resize(size)
        # new_size.save(saved + f"_new_size_{size[0]}_size{size[1]}" + ext)
        # new_size.save()
        # original.resize_image = saved + f'_new_size{size}' + ext
        original.resize_image = new_size
        original.save(original.resize_image)
        original_temp_image.close()

    except FileNotFoundError:
        print("File not found")



