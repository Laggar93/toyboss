from django.shortcuts import render
from .models import ProductionPage, Advantages, Points


def production_view(request):

    content = {
        'production_page': ProductionPage.objects.first(),
        'advantages': Advantages.objects.first(),
        'points': Points.objects.all(),
        'link_ru': '/ru/production/',
        'link_en': '/en/production/',
        'link_kg': '/ky/production/',

    }

    return render(request, 'production.html', content)