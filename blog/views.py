from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
# Create your views here.
from .models import Category, Post, Tag


def blog(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    posts_paginated = pagination(request, posts)
    return render(request, 'blog/blog.html', {'posts': posts_paginated})


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    if post.category.slug != category_slug:
        raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category_selected = get_object_or_404(Category, slug=slug)
    posts = category_selected.posts.filter(status=Post.ACTIVE)
    posts_paginated = pagination(request, posts)
    return render(request, 'blog/category.html', {'category': category_selected, 'posts': posts_paginated})


def tags(request, slug):
    tag_selected = get_object_or_404(Tag, slug=slug)
    posts = tag_selected.posts.filter(status=Post.ACTIVE)
    posts_paginated = pagination(request, posts)
    return render(request, 'blog/tags.html', {'tag': tag_selected, 'posts': posts_paginated})


def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query),
                                status=Post.ACTIVE)
    posts_paginated = pagination(request, posts)
    return render(request, 'blog/search.html', {'posts': posts_paginated, 'query': query})


#UTIL
def pagination(request, posts):
    page = request.GET.get('page', '1')
    page_limit = request.GET.get('limit', '10')

    if not (page_limit.isdigit() and int(page_limit) > 0):
        page_limit = '10'
    posts_paginator = Paginator(posts, page_limit)
    try:
        return posts_paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        return redirect('blog')
