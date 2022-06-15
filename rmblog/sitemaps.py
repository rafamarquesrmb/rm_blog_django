from django.contrib.sitemaps import Sitemap

from django.shortcuts import reverse

from blog.models import Category, Post, Tag


class TagSitemap(Sitemap):
    def items(self):
        return Tag.objects.all()


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        return obj.created_at
