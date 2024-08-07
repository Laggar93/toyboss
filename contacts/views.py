from django.shortcuts import render
from .models import ContactsPage, SocialNetwork, Schedule, MarketingDepartment, ProductionDepartment, \
    Accounting, CentralOffice, CorporateOffice


def contacts_view(request):

    content = {
        'contacts_page': ContactsPage.objects.first(),
        'social_network': SocialNetwork.objects.first(),
        'schedule': Schedule.objects.first(),
        'marketing_department': MarketingDepartment.objects.first(),
        'production_department': ProductionDepartment.objects.first(),
        'accounting': Accounting.objects.first(),
        'central_office': CentralOffice.objects.first(),
        'corporate_office': CorporateOffice.objects.first(),
        'link_ru': '/ru/contacts/',
        'link_en': '/en/contacts/',
        'link_kg': '/ky/contacts/',
    }

    return render(request, 'contacts.html', content)