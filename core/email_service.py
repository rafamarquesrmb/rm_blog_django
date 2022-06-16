import datetime

from django.core.mail import send_mail
from decouple import config


def send_contact_email(message_form):
    subject = "Message received from RMBlog"
    message = f"Message received from RMBlog ||| " \
              f"NAME: {message_form.cleaned_data['name']} ||| " \
              f"EMAIL: {message_form.cleaned_data['email']} ||| " \
              f"PHONE: {message_form.cleaned_data['phone']} ||| " \
              f"MESSAGE: {message_form.cleaned_data['message']} ||| " \
              f">Date: {datetime.datetime.now()}   "
    html_mesage = f"Message received from RMBlog <br/>" \
                  f"<strong>NAME:</strong> {message_form.cleaned_data['name']}<br/><br/>" \
                  f"<strong>EMAIL:</strong> {message_form.cleaned_data['email']}<br/><br/>" \
                  f"<strong>PHONE:</strong> {message_form.cleaned_data['phone']}<br/><br/>" \
                  f"<strong>MESSAGE:</strong> {message_form.cleaned_data['message']}<br/><br/>" \
                  f"<strong>Date: </strong>{datetime.datetime.now()}"
    from_email = config('EMAIL_HOST')
    to_email = [config('EMAIL_HOST_USER')]
    send_mail(subject=subject, message=message, html_message=html_mesage, from_email=from_email,
              recipient_list=to_email)


def new_subscriber_email(subscriber_form):
    path = "https://rmblog.example/unsub/"
    subject = "Thank you for subscribing to RM Blog Newsletter!"
    message = f"Hi! I'm Rafael Marques from RM Blog! <br/>" \
              f"I'm glad you subscribed to the RM Blog Newsletter! <br/>" \
              f"Follow your email to receive the news. <br/>" \
              f"<br/><br/><hr/><br/>" \
              f"<small>This is an automated message! You are receiving because you signed up for the RM Blog Newsletter." \
              f'If you no longer wish to receive our messages, you can <a href="{path}/{subscriber_form.cleaned_data["unsubscribe_key"]}" target="_blank" >unsubscribe by clicking here.</a></small><br/><br/>'

    from_email = config('EMAIL_HOST')
    to_email = subscriber_form.cleaned_data['email']
    send_mail(subject=subject, message=message, html_message=message, from_email=from_email,
              recipient_list=to_email)


def new_subscriber_to_host(new_subscriber_form):
    subject = "New Subscriber from RMBlog"
    message = f"Message received from RMBlog ||| " \
              f"New Subscriber on RM Blog! " \
              f"EMAIL: {new_subscriber_form.cleaned_data['email']} ||| " \
              f">Date: {datetime.datetime.now()}"
    html_mesage = f"Message received from RMBlog <br/>" \
                  f"New Subscriber on RM Blog! <br/>" \
                  f"<strong>EMAIL:</strong> {new_subscriber_form.cleaned_data['email']}<br/><br/>" \
                  f"<strong>Date: </strong>{datetime.datetime.now()}"
    from_email = config('EMAIL_HOST')
    to_email = [config('EMAIL_HOST_USER')]
    send_mail(subject=subject, message=message, html_message=html_mesage, from_email=from_email,
              recipient_list=to_email)
