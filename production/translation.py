from modeltranslation.translator import translator, TranslationOptions
from .models import *


class ProductionPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title')
    required_languages = {'ky': ('title', 'page_title'),
                          'en': ('title', 'page_title')}


class AdvantagesTranslationOptions(TranslationOptions):
    fields = ('main_title', 'first_advantage', 'second_advantage', 'third_advantage',
              'fourth_advantage', 'fifth_advantage', 'sixth_advantage')
    required_languages = {'ky': ('main_title', 'first_advantage', 'second_advantage', 'third_advantage',
              'fourth_advantage', 'fifth_advantage', 'sixth_advantage'),
                          'en': ('main_title', 'first_advantage', 'second_advantage', 'third_advantage',
              'fourth_advantage', 'fifth_advantage', 'sixth_advantage')}


class PointsTranslationOptions(TranslationOptions):
    fields = ('point_title', 'text')
    required_languages = {'ky': ('point_title', 'text'),
                          'en': ('point_title', 'text')}


translator.register(ProductionPage, ProductionPageTranslationOptions)
translator.register(Advantages, AdvantagesTranslationOptions)
translator.register(Points, PointsTranslationOptions)