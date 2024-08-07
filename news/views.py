from django.shortcuts import render, get_object_or_404
from .models import NewsPage, NewsItem
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def news_page_view(request):
    all_news = NewsItem.objects.all().order_by('-published')
    paginator = Paginator(all_news, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    content = {
        'news_page': NewsPage.objects.first(),
        'news_items': NewsItem.objects.all().order_by('-published'),
        'page_obj': page_obj,
        'link_ru': '/ru/news/',
        'link_en': '/en/news/',
        'link_kg': '/ky/news/',
    }

    return render(request, 'news.html', content)


def news_view_detail(request, news_item_slug):

    link_ru = f'/ru/news/{news_item_slug}/'
    link_en = f'/en/news/{news_item_slug}/'
    link_ky = f'/ky/news/{news_item_slug}/'

    current_news = get_object_or_404(NewsItem, slug=news_item_slug)

    content = {
        'current_news': current_news,
        'other_news': NewsItem.objects.exclude(slug=news_item_slug),
        'news_page': NewsPage.objects.first(),
        'link_ru': link_ru,
        'link_en': link_en,
        'link_kg': link_ky,

    }

    return render(request, 'news-detail.html', content)