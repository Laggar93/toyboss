from django.http import JsonResponse
from django.shortcuts import render, redirect

from toyboss.sendform import send_coop_form
from .forms import CoopForm
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


def coop_form_view(request):
    if request.method == 'POST':
        form = CoopForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            position = form.cleaned_data['position']
            text = form.cleaned_data['text']
            file = form.cleaned_data.get('file')
            send_coop_form(name, phone, position, text, file)
            success_message = 'Спасибо, ваша заявка успешно отправлена'
            return JsonResponse({'success_message': success_message})
        else:
            return JsonResponse({'form_errors': form.errors}, status=400)

    return redirect('/')