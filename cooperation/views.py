from django.shortcuts import render
from .models import CooperationPage, Wholesale, Retailsale, Partners, CooperationForm


def cooperation_view(request):

    content = {
        'cooperation_page': CooperationPage.objects.first(),
        'wholesale': Wholesale.objects.first(),
        'retailsale': Retailsale.objects.first(),
        'partners': Partners.objects.first(),
        'cooperation_form': CooperationForm.objects.first(),
        'link_ru': '/ru/cooperation/',
        'link_en': '/en/cooperation/',
        'link_kg': '/ky/cooperation/',

    }

    return render(request, 'cooperation.html', content)