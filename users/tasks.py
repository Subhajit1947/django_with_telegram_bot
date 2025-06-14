from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings

@shared_task(bind=True, name='send_welcome_email', max_retries=3)
def send_welcome_email(self, email):
    
    try:
        subject = 'Welcome to Our Platform!'
        context = {
            'email': email,
        }
        
        html_message = render_to_string('emails/welcome_email.html', context)
        plain_message = strip_tags(html_message)
        
        send_mail(
            subject=subject,
            message=plain_message,
            html_message=html_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        return f"Welcome email sent to {email}"
        
    except Exception as e:
        self.retry(exc=e, countdown=60 * self.request.retries)  # Exponential backoff