from django.shortcuts import render
from .models import ProductCategory, Products, ProductPage


def products_view(request):

    content = {
        'product_page': ProductPage.objects.first(),
        'product_categories': ProductCategory.objects.all(),
        'products': Products.objects.all(),
        'link_ru': '/ru/products/',
        'link_en': '/en/products/',
        'link_kg': '/ky/products/',

    }

    return render(request, 'catalog.html', content)

