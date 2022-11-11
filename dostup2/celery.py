from celery import Celery
import os
from celery.schedules import crontab
#
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dostup2.settings')


app = Celery('dostup2')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'spam_task': {
        'task': 'dostup2app.tasks.schedule_task',
        'schedule': crontab(minute='*/1')
    }
}
