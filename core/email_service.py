import datetime

from django.core.mail import send_mail
from decouple import config


def send_contact_email(MessageForm):
    subject = "Message received from RMBlog"
    message = f"Message received from RMBlog ||| " \
              f"NAME: {MessageForm.cleaned_data['name']} ||| " \
              f"EMAIL: {MessageForm.cleaned_data['email']} ||| " \
              f"PHONE: {MessageForm.cleaned_data['phone']} ||| " \
              f"MESSAGE: {MessageForm.cleaned_data['message']} ||| " \
              f">Date: {datetime.datetime.now()}   "
    html_mesage = f"Message received from RMBlog <br/>" \
              f"<strong>NAME:</strong> {MessageForm.cleaned_data['name']}<br/><br/>" \
              f"<strong>EMAIL:</strong> {MessageForm.cleaned_data['email']}<br/><br/>" \
              f"<strong>PHONE:</strong> {MessageForm.cleaned_data['phone']}<br/><br/>" \
              f"<strong>MESSAGE:</strong> {MessageForm.cleaned_data['message']}<br/><br/>" \
              f"<strong>Date: </strong>{datetime.datetime.now()}"
    from_email = config('EMAIL_HOST')
    to_email = [config('EMAIL_HOST_USER')]
    send_mail(subject = subject, message=message, html_message=html_mesage, from_email=from_email, recipient_list= to_email)
