import os
from celery import Celery

# Setting the environment variable containing the name of the settings file for our project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.setting')

app = Celery('myshop')

app.config_from_objects('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
