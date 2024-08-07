from django.shortcuts import render
from .models import AboutPage, History, Years, Mission, Vision, Value, ValuePoints, \
    StatisticPoints, Certificates, Rewards, Statistic


def about_view(request):

    content = {
        'about_page': AboutPage.objects.first(),
        'history': History.objects.first(),
        'years': Years.objects.all(),
        'mission': Mission.objects.first(),
        'vision': Vision.objects.first(),
        'value': Value.objects.first(),
        'value_points': ValuePoints.objects.first(),
        'statistic_points': StatisticPoints.objects.all(),
        'statistic': Statistic.objects.first(),
        'certificates': Certificates.objects.first(),
        'rewards': Rewards.objects.first(),
        'link_ru': '/ru/about/',
        'link_en': '/en/about/',
        'link_kg': '/ky/about/',

    }

    return render(request, 'about-us.html', content)