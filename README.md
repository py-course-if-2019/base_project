# image_storage

Near manage.py
```celery -A images_storage worker -l info``` - to run worker
```celery purge -A images_storage``` - clean queue