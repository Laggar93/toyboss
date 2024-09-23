from modeltranslation.translator import translator, TranslationOptions
from .models import *


class MainCooperationTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'first_city', 'second_city')
    required_languages = {'ky': ('title', 'subtitle', 'first_city', 'second_city'),
                          'en': ('title', 'subtitle', 'first_city', 'second_city')}


class MainPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords')
    required_languages = {'ky': ('title',),
                          'en': ('title',)}


class MainPageSliderTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class GroupsTranslationOptions(TranslationOptions):
    fields = ('title', 'sandwich_text', 'toyboss_text', 'agrokush_text', 'broiler_text')
    required_languages = {'ky': ('title', 'sandwich_text', 'toyboss_text', 'agrokush_text', 'broiler_text'),
                          'en': ('title', 'sandwich_text', 'toyboss_text', 'agrokush_text', 'broiler_text')}


class MainProdTranslationOptions(TranslationOptions):
    fields = ('title', 'top_text', 'bottom_text')
    required_languages = {'ky': ('title', 'top_text', 'bottom_text'),
                          'en': ('title', 'top_text', 'bottom_text')}


class SurveyTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button_name')
    required_languages = {'ky': ('title', 'subtitle', 'button_name'),
                          'en': ('title', 'subtitle', 'button_name')}


class MainQuoteTranslationOptions(TranslationOptions):
    fields = ('first_line', 'second_line', 'third_line', 'first_name', 'position', 'history_title', 'history_text', 'mission_title', 'mission_text', 'value_title', 'value_text')
    required_languages = {'ky': ('first_line', 'second_line', 'third_line', 'first_name', 'position', 'history_title', 'history_text', 'mission_title', 'mission_text', 'value_title', 'value_text'),
                          'en': ('first_line', 'second_line', 'third_line', 'first_name', 'position', 'history_title', 'history_text', 'mission_title', 'mission_text', 'value_title', 'value_text')}



translator.register(MainCooperation, MainCooperationTranslationOptions)
translator.register(MainPage, MainPageTranslationOptions)
translator.register(MainPageSlider, MainPageSliderTranslationOptions)
translator.register(Groups, GroupsTranslationOptions)
translator.register(MainProd, MainProdTranslationOptions)
translator.register(MainQuote, MainQuoteTranslationOptions)
translator.register(Survey, SurveyTranslationOptions)