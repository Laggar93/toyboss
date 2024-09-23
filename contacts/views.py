from django.shortcuts import render, redirect
from django.http import JsonResponse
from toyboss.sendform import send_form
from .forms import ContactForm as ContactPageForm
from .models import ContactsPage, SocialNetwork, Schedule, MarketingDepartment, ProductionDepartment, \
    Accounting, CentralOffice, CorporateOffice, ContactForm


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
        'contact_form': ContactForm.objects.first(),
        'link_ru': '/ru/contacts/',
        'link_en': '/en/contacts/',
        'link_kg': '/ky/contacts/',
    }

    return render(request, 'contacts.html', content)


def form_view(request):
    if request.method == 'POST':
        form = ContactPageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            text = form.cleaned_data['text']
            send_form(name, email, phone, text)
            success_message = 'Спасибо, ваша заявка успешно отправлена'
            return JsonResponse({'success_message': success_message})
        else:
            return JsonResponse({'form_errors': form.errors}, status=400)

    return redirect('/')
