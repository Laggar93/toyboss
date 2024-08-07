from modeltranslation.translator import translator, TranslationOptions
from .models import *


class CooperationPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title', 'left_text', 'right_text')
    required_languages = {'ky': ('title', 'page_title', 'left_text', 'right_text'),
                          'en': ('title', 'page_title', 'left_text', 'right_text')}


class WholesaleTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'first_city', 'second_city')
    required_languages = {'ky': ('title', 'subtitle', 'first_city', 'second_city'),
                          'en': ('title', 'subtitle', 'first_city', 'second_city')}


class RetailsaleTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'first_city', 'second_city')
    required_languages = {'ky': ('title', 'subtitle', 'first_city', 'second_city'),
                          'en': ('title', 'subtitle', 'first_city', 'second_city')}


class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')
    required_languages = {'ky': ('title', 'subtitle'),
                          'en': ('title', 'subtitle')}


class CooperationFormTranslationOptions(TranslationOptions):
    fields = ('main_title', 'subtitle', 'name', 'phone', 'position', 'message', 'rules', 'file', 'send_button')
    required_languages = {'ky': ('main_title', 'subtitle', 'name', 'phone', 'position', 'message', 'rules', 'file', 'send_button'),
                          'en': ('main_title', 'subtitle', 'name', 'phone', 'position', 'message', 'rules', 'file', 'send_button')}


translator.register(CooperationPage, CooperationPageTranslationOptions)
translator.register(Wholesale, WholesaleTranslationOptions)
translator.register(Retailsale, RetailsaleTranslationOptions)
translator.register(Partners, PartnersTranslationOptions)
translator.register(CooperationForm, CooperationFormTranslationOptions)