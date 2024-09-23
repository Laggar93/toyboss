from contacts.models import SocialNetwork
from news.models import NewsPage
from production.models import Advantages
from about.models import StatisticPoints, Statistic
from product.models import ProductCategory, Products, ProductPage
from blocks.models import NavigationMenu, Footer, NotFound, GeneralTranslations
from toyboss.config import site_name


def globals(request):

    context = {
        'advantages': Advantages.objects.first(),
        'statistic_points': StatisticPoints.objects.all(),
        'statistic': Statistic.objects.first(),
        'product_page': ProductPage.objects.first(),
        'product_categories': ProductCategory.objects.all(),
        'products': Products.objects.all(),
        'navigation_menu': NavigationMenu.objects.first(),
        'footer': Footer.objects.first(),
        'not_found': NotFound.objects.first(),
        'social_network': SocialNetwork.objects.first(),
        'general_translations': GeneralTranslations.objects.first(),
        'news_page': NewsPage.objects.first(),
        'site_name': site_name,
    }

    return context