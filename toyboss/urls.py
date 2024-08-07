from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from toyboss import settings
from toyboss.config import admin_url
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path(admin_url + '/', admin.site.urls),

]


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