from celery import shared_task
from django.core.mail import EmailMessage
import logging
from django.template.loader import render_to_string
from .models import *
from datetime import datetime

logger = logging.getLogger(__name__)
@shared_task(name="email_task")
def send_email_task(subject,body,subscriber_email):

        email = EmailMessage(
            subject,
            body,
            to=[subscriber_email]
        )

        email.send(fail_silently=False)
        print(f"Email sent successfully to {subscriber_email}")
        logger.info(f"✅ Email sent successfully to {subscriber_email}")
        return subscriber_email

@shared_task(name='monthly_newsletter')
def send_newsletter():
    subject = "Your Monthly Newsletter"
    subscribers=MessageBoard.objects.get(id=1).subscribers.all()
    
    # subscribers = MessageBoard.objects.get(id=1).subscribers.filter(
    #     profile__newsletter_subscribed=True,
    # )
    
    for subscriber in subscribers:
        body = render_to_string('a_messageboard/newsletter.html', {'name': subscriber.profile.name})
        email = EmailMessage( subject, body, to=[subscriber.email] )
        email.content_subtype = "html"
        email.send()
    
    current_month = datetime.now().strftime('%B') 
    subscriber_count = subscribers.count()   
    return f'{current_month} Newsletter to {subscriber_count} subs'