from core.views import about, contact, custom_404, homepage, robots_txt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
                  path('robots.txt', robots_txt, name='robots_txt'),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('about/', about, name='about'),
                  path('contact/', contact, name='contact'),
                  path('', homepage, name='homepage'),
                  path('blog/', include('blog.urls')),
                  path('newsletter/', include('newsletter.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_404
