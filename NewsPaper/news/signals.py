from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory
from .tasks import send_notifications_task

SITE_URL = 'http://127.0.0.1:8000'


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        send_notifications_task.delay(instance.pk)
