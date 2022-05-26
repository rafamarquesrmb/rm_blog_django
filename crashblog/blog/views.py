from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.db.models import Q
# Create your views here.
from .models import Post, Category
from .forms import CommentForm


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    if post.category.slug != category_slug:
        raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category_selected = get_object_or_404(Category, slug=slug)
    posts = category_selected.posts.filter(status=Post.ACTIVE)
    return render(request, 'blog/category.html', {'category': category_selected, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query), status=Post.ACTIVE)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})
