import uuid

from django.db import models


# Create your models here.
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    inscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribe_key = models.UUIDField(auto_created=True,blank=True, unique=True)

    class Meta:
        ordering = ('email',)
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email


