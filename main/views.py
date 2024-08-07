from django.shortcuts import render
from faq.models import FaqPage, Questions
from production.models import Advantages
from about.models import StatisticPoints, Statistic, Certificates, AboutPage, History, Mission, Vision
from product.models import ProductCategory, Products, ProductPage
from news.models import NewsPage, NewsItem
from .models import MainPage, Groups, MainProd, MainCooperation, MainPageSlider, MainQuote


def main_view(request):
    link_kg = '/ky/'
    link_ru = '/ru/'
    link_en = '/en/'

    content = {
        'main_page': MainPage.objects.first(),
        'main_prod': MainProd.objects.first(),
        'main_page_slider': MainPageSlider.objects.all().order_by('order'),
        'main_cooperation': MainCooperation.objects.first(),
        'news_page': NewsPage.objects.first(),
        'news_items': NewsItem.objects.all().order_by('-published')[:4],
        'advantages': Advantages.objects.first(),
        'statistic_points': StatisticPoints.objects.all(),
        'statistic': Statistic.objects.first(),
        'product_page': ProductPage.objects.first(),
        'product_categories': ProductCategory.objects.all(),
        'products': Products.objects.all(),
        'certificates': Certificates.objects.first(),
        'faq_page': FaqPage.objects.first(),
        'questions': Questions.objects.filter(show_main_page=True),
        'groups': Groups.objects.first(),
        'about_page': AboutPage.objects.first(),
        'history': History.objects.first(),
        'mission': Mission.objects.first(),
        'vision': Vision.objects.first(),
        'main_quote': MainQuote.objects.first(),
        'link_kg': link_kg,
        'link_ru': link_ru,
        'link_en': link_en,
    }

    return render(request, 'index1.html', content)
