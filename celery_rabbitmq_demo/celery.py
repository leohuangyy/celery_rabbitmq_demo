from __future__ import absolute_import

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_rabbitmq_demo.settings')

app=Celery('celery_rabbitmq_demo')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()


