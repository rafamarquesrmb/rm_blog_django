from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from blog.models import Post

# Create your views here.
from core.email_service import send_contact_email
from core.forms import MessageForm


def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)[:3]
    return render(request, 'core/frontpage.html', {'posts': posts})


def about(request):
    return render(request, 'core/about.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /newsletter/",
        "Disallow: /tinymce/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")


def contact(request):
    email_form = MessageForm()
    if request.method == "POST":
        email_form = MessageForm(request.POST)
        if email_form.is_valid():
            try:
                send_contact_email(email_form)
                email_form = MessageForm()
                messages.success(request, "Your message has been sent successfully!")
            except:
                messages.error(request, "Sorry. Something went wrong. Please try again.")
        else:
            messages.warning(request, "Please fill in the fields correctly")
    context = {
        'form': email_form,
    }
    return render(request, 'core/contact.html', context)


def error_404_view(request, exception):
    return render(request, 'core/404.html')
