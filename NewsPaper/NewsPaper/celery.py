import os
from celery import Celery
from celery.schedules import crontab

# celery -A NewsPaper worker -l INFO --pool=solo
# celery -A NewsPaper beat -l INFO


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.sending_notifications_every_mon_at_8_am_task',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}

app.autodiscover_tasks()
