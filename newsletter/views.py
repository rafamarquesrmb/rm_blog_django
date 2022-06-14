import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import NewsletterSubscriber


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        if not email:
            messages.error(request, "Email is required")
            return redirect(request.POST.get('next', '/'))
        subscriber = NewsletterSubscriber()
        subscriber.email = email
        new_key = uuid.uuid4()
        key_exists = True
        while key_exists:
            obj_exists = NewsletterSubscriber.objects.filter(unsubscribe_key=new_key)
            if obj_exists:
                new_key = uuid.uuid4()
            else:
                key_exists = False
        subscriber.unsubscribe_key = new_key
        try:
            subscriber.save()
            # Send 'thanks' email
            messages.success(request, "Congratulations! You have been registered in our newsletter! Follow your email to receive the news!")
        except:
            messages.error(request, "Sorry... There was an error in the request. Please try again.")
    return redirect(request.POST.get('next', '/'))




def unsubscribe(request):
    if request.method == 'POST':
        key = request.POST.get("key")
        subscriber = NewsletterSubscriber.objects.filter(unsubscribe_key=key)
        if subscriber:
            try:
                messages.error(request, "Sorry... There was an error in the request. Please try again.")
                subscriber.delete()
            except:
                pass
                messages.error(request, "Sorry... There was an error in the request. Please try again.")
            return redirect('home', )
        else:
            # go to another page
            pass
