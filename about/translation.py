from modeltranslation.translator import translator, TranslationOptions
from .models import *


class AboutPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title')
    required_languages = {'ky': ('title', 'page_title'),
                          'en': ('title', 'page_title')}


class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
    required_languages = {'ky': ('title', 'text'),
                          'en': ('title', 'text')}


class YearsTranslationOptions(TranslationOptions):
    fields = ('description',)
    required_languages = {'ky': ('description',),
                          'en': ('description',)}


class MissionTranslationOptions(TranslationOptions):
    fields = ('title', 'quote', 'text')
    required_languages = {'ky': ('title', 'quote', 'text'),
                          'en': ('title', 'quote', 'text')}


class VisionTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
    required_languages = {'ky': ('title', 'text'),
                          'en': ('title', 'text')}


class ValueTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
    required_languages = {'ky': ('title', 'text'),
                          'en': ('title', 'text')}


class ValuePointsTranslationOptions(TranslationOptions):
    fields = ('first_title', 'first_text', 'second_title', 'second_text',
              'third_title', 'third_text', 'fourth_title', 'fourth_text',
              'fifth_title', 'fifth_text')
    required_languages = {'ky': ('first_title', 'first_text', 'second_title', 'second_text',
                                 'third_title', 'third_text', 'fourth_title', 'fourth_text',
                                 'fifth_title', 'fifth_text'),
                          'en': ('first_title', 'first_text', 'second_title', 'second_text',
                                 'third_title', 'third_text', 'fourth_title', 'fourth_text',
                                 'fifth_title', 'fifth_text')}


class StatisticPointsTranslationOptions(TranslationOptions):
    fields = ('title', 'left_postscript', 'right_postscript',
              'subtitle')
    required_languages = {'ky': ('title',
                                 'subtitle'),
                          'en': ('title',
                                 'subtitle')}


class CertificatesItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CertificatesTranslationOptions(TranslationOptions):
    fields = ('title', 'button_name')
    required_languages = {'ky': ('title', 'button_name'),
                          'en': ('title', 'button_name')}


class RewardsTranslationOptions(TranslationOptions):
    fields = ('title', 'button_name')
    required_languages = {'ky': ('title', 'button_name'),
                          'en': ('title', 'button_name')}


class StatisticTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = {'ky': ('title',),
                          'en': ('title',)}


translator.register(AboutPage, AboutPageTranslationOptions)
translator.register(History, HistoryTranslationOptions)
translator.register(Years, YearsTranslationOptions)
translator.register(Mission, MissionTranslationOptions)
translator.register(Vision, VisionTranslationOptions)
translator.register(Value, ValueTranslationOptions)
translator.register(ValuePoints, ValuePointsTranslationOptions)
translator.register(StatisticPoints, StatisticPointsTranslationOptions)
translator.register(Certificates, CertificatesTranslationOptions)
translator.register(CertificatesItems, CertificatesItemsTranslationOptions)
translator.register(Rewards, RewardsTranslationOptions)
translator.register(Statistic, StatisticTranslationOptions)
