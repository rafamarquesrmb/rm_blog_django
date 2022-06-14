import uuid

from django.contrib import admin

# Register your models here.
from newsletter.models import NewsletterSubscriber


class NewsletterSubscriberAdmin(admin.ModelAdmin):
    search_fields = ['email', 'inscribed_at', 'unsubscribe_key']
    list_display = ['email', 'inscribed_at', 'unsubscribe_key']
    list_filter = ['inscribed_at']
    fields = ['email', 'inscribed_at', 'unsubscribe_key']
    readonly_fields = ['inscribed_at', 'unsubscribe_key']

    def save_model(self, request, obj, form, change):
        new_key = uuid.uuid4()
        key_exists = True
        while (key_exists):
            obj_exists = NewsletterSubscriber.objects.filter(unsubscribe_key=new_key)
            if obj_exists:
                new_key = uuid.uuid4()
            else:
                key_exists = False
        obj.unsubscribe_key = new_key
        super().save_model(request, obj, form, change)


admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
