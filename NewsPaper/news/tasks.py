import datetime
from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, Category

SITE_URL = 'http://127.0.0.1:8000'


@shared_task
def send_notifications_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    heading = post.heading
    preview = post.preview()

    subscribers = []

    for category in categories:
        subscribers += category.subscribers.all()

    subscribers = [s.email for s in subscribers]

    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/{pk}',
        }
    )

    for sub in subscribers:
        msg = EmailMultiAlternatives(
            subject=heading,
            body='',
            from_email='news_paper@example.org',
            to=[sub],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@shared_task
def sending_notifications_every_mon_at_8_am_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(created_at__gte=last_week)
    categories = set(posts.values_list('category__category_name', flat=True))
    subscribers = set(
        Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True)
    )
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': SITE_URL,
            'posts': posts,

        }
    )

    for sub in subscribers:
        msg = EmailMultiAlternatives(
            subject='Подборка статей за неделю',
            body='',
            from_email='news_paper@example.org',
            to=[sub],
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
