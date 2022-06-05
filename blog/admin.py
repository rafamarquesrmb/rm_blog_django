from django.contrib import admin
from .models import Post, Category, Comment, Tag


# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status', ]
    list_filter = ['category', 'created_at', 'status', ]
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
