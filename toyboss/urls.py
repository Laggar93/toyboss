from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from blocks.views import sitemap_view, robots_view, handle404
from toyboss import settings
from toyboss.config import admin_url
from django.conf.urls.i18n import i18n_patterns
from contacts.views import form_view
from cooperation.views import coop_form_view


urlpatterns = [
    path(admin_url + '/', admin.site.urls),
    path('sitemap.xml', sitemap_view, name='sitemap_view'),
    path('robots.txt', robots_view, name='robots_view'),
    path('form/', form_view, name='form'),
    path('cooperation-form/', coop_form_view, name='form'),

]


handler404=handle404


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('', include('about.urls')),
    path('', include('production.urls')),
    path('', include('news.urls')),
    path('', include('product.urls')),
    path('', include('contacts.urls')),
    path('', include('cooperation.urls')),
    path('', include('faq.urls')),
)
