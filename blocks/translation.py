from modeltranslation.translator import translator, TranslationOptions
from .models import *


class NavigationMenuTranslationOptions(TranslationOptions):
    fields = ('about', 'production', 'product', 'cooperation', 'news', 'contact', 'faq', 'ustukan_game_general', 'ustukan_game_first', 'ustukan_game_second')
    required_languages = {'ky': ('about', 'production', 'product', 'cooperation', 'news', 'contact', 'faq', 'ustukan_game_general'),
                          'en': ('about', 'production', 'product', 'cooperation', 'news', 'contact', 'faq', 'ustukan_game_general')}


class FooterTranslationOptions(TranslationOptions):
    fields = ('title', 'rights', 'office_title', 'address', 'phone_title')
    required_languages = {'ky': ('title', 'rights', 'office_title', 'address', 'phone_title'),
                          'en': ('title', 'rights', 'office_title', 'address', 'phone_title')}


class NotFoundTranslationOptions(TranslationOptions):
    fields = ('page_not_found_first', 'page_not_found_second', 'to_main')
    required_languages = {'ky': ('page_not_found_first', 'page_not_found_second', 'to_main'),
                          'en': ('page_not_found_first', 'page_not_found_second', 'to_main')}


class GeneralTranslationsTranslationOptions(TranslationOptions):
    fields = ('detail_button', 'product_description', 'product_compound', 'product_all')
    required_languages = {'ky': ('detail_button', 'product_description', 'product_compound', 'product_all'),
                          'en': ('detail_button', 'product_description', 'product_compound', 'product_all')}


translator.register(NavigationMenu, NavigationMenuTranslationOptions)
translator.register(Footer, FooterTranslationOptions)
translator.register(NotFound, NotFoundTranslationOptions)
translator.register(GeneralTranslations, GeneralTranslationsTranslationOptions)