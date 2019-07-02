web: images_storage/manage.py migrate && python images_storage/manage.py runserver 0.0.0.0:$PORT

worker: celery worker --app=images_storage.celery.app