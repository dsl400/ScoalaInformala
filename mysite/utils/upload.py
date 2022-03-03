import os
from django.conf import settings


def store_uploaded_file(file,user_id):
    destination_dir = os.path.join(settings.MEDIA_ROOT, settings.MEDIA_PROFILE_IMAGES)
    os.makedirs(destination_dir, exist_ok=True)
    f_name = f'{user_id}_{file.name}'
    with open(os.path.join(destination_dir, f_name) , 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return f'/media/{settings.MEDIA_PROFILE_IMAGES}/{f_name}'