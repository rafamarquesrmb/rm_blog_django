from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)[:3]
    return render(request, 'core/frontpage.html', {'posts': posts})


def about(request):
    return render(request, 'core/about.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

def contact(request):
    return render(request, 'core/contact.html')

def error_404_view(request, exception):
    return render(request, 'core/404.html')
