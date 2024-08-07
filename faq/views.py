from django.shortcuts import render
from .models import FaqPage, Questions
from main.models import MainCooperation


def faq_view(request):

    content = {
        'faq_page': FaqPage.objects.first(),
        'main_cooperation': MainCooperation.objects.first(),
        'questions': Questions.objects.all(),
        'link_ru': '/ru/faq/',
        'link_en': '/en/faq/',
        'link_kg': '/ky/faq/',

    }

    return render(request, 'faq.html', content)