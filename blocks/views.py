from django.shortcuts import render
from news.models import NewsItem
from .models import NotFound
from toyboss import config


def sitemap_view(request):

    content = {
        'news_items': NewsItem.objects.all(),
    }

    return render(request, 'sitemap.xml', content, content_type='text/xml')


def robots_view(request):

    content = {
        'site_name': config.site_name,
    }
    return render(request, 'robots.txt', content, content_type='text/plain')


def handle404(request, exception):
    page_not_found = NotFound.objects.first()

    content = {
        'not_found': page_not_found
    }
    return render(request, '404.html', content, status=404)