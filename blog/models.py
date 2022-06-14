from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=60, unique=True, null=False, blank=False)
    meta_description = models.CharField(max_length=155, null=True, blank=True)
    slug = models.SlugField(unique=True, null=False, blank=False)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug


class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    COICHES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=60, blank=False, unique=True, null=False)
    meta_description = models.CharField(max_length=155, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=False, null=False)
    intro = models.TextField(blank=True)
    body = RichTextUploadingField(blank=True, null=True, config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=COICHES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    tags = models.ManyToManyField("Tag", related_name="posts")
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return_str = 'by ' + self.name + ' | at: ' + self.post.title
        return return_str


class Tag(models.Model):
    title = models.CharField(unique=True, max_length=60, blank=False, null=False)
    meta_description = models.CharField(max_length=155, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=False, null=False)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug
