from production.models import Advantages
from about.models import StatisticPoints, Statistic
from product.models import ProductCategory, Products, ProductPage


def globals(request):

    context = {
        'advantages': Advantages.objects.first(),
        'statistic_points': StatisticPoints.objects.all(),
        'statistic': Statistic.objects.first(),
        'product_page': ProductPage.objects.first(),
        'product_categories': ProductCategory.objects.all(),
        'products': Products.objects.all(),
    }

    return context