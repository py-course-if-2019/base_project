web: images_storage/manage.py migrate && python images_storage/manage.py runserver 0.0.0.0:$PORT

worker: cd images_storage && celery -A images_storage worker -l info