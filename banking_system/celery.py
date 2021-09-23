# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

from celery import Celery
import os

# Set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_system.settings')

app = Celery('banking_system', backend='redis://localhost', broker='pyamqp://')

# Using a string here means the worker doesn't have to serialize the
# configuration object to child processes. namespace='CELERY' means
# all celery-related configuration keys should have a 'CELERY_' prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs
app.autodiscover_tasks()



