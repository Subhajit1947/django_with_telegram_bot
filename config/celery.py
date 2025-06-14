import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('bot_project')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_time_limit = 300
app.autodiscover_tasks()

