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
    context = {
        'page_title': 'Blog',
        'page_metatitle': 'A blog about Programming and technology.',
        'banner_background_image_slug': 'assets/img/home-bg.jpg',
        'banner_heading': 'RM Blog',
        'banner_subheading': 'A blog about Programming and technology.',
        'posts': posts_paginated,
    }
    return render(request, 'blog/posts.html', context)


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
    context = {
        'page_title': f'Tag: {category_selected.title}',
        'page_metatitle': category_selected.meta_description,
        'banner_background_image_slug': 'assets/img/home-bg.jpg',
        'banner_heading': category_selected.title,
        'banner_subheading': f'Showing all posts of the "{category_selected.title}" tag',
        'posts': posts_paginated,
    }
    return render(request, 'blog/posts.html', context)


def tags(request, slug):
    tag_selected: Tag = get_object_or_404(Tag, slug=slug)
    posts = tag_selected.posts.filter(status=Post.ACTIVE)
    posts_paginated = pagination(request, posts)
    context = {
        'page_title': f'Tag: {tag_selected.title}',
        'page_metatitle': tag_selected.meta_description,
        'banner_background_image_slug': 'assets/img/home-bg.jpg',
        'banner_heading': tag_selected.title,
        'banner_subheading': f'Showing all posts of the "{tag_selected.title}" tag',
        'posts': posts_paginated,
    }
    return render(request, 'blog/posts.html', context)


def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query),
                                status=Post.ACTIVE)
    posts_paginated = pagination(request, posts)
    subheading = f'Showing all search results for: "{query}"'
    context = {
        'page_title': 'Search Results',
        'page_metatitle': 'Meta Description',
        'banner_background_image_slug': 'assets/img/home-bg.jpg',
        'banner_heading': 'Search Results',
        'banner_subheading': subheading,
        'posts': posts_paginated,
    }
    return render(request, 'blog/posts.html', context)


# UTIL
def pagination(request, posts):
    # SETTINGS:
    default_page = 1
    default_limit = 2

    page = request.GET.get('page', f'{default_page}')
    page_limit = request.GET.get('limit', f'{default_limit}')

    if not (page_limit.isdigit() and int(page_limit) > 0):
        page_limit = f'{default_limit}'
    posts_paginator = Paginator(posts, page_limit)
    try:
        return posts_paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        return redirect('blog')
