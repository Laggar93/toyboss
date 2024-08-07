from modeltranslation.translator import translator, TranslationOptions
from .models import *


class FaqPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title')
    required_languages = {'ky': ('title', 'page_title'),
                          'en': ('title', 'page_title')}


class QuestionsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
    required_languages = {'ky': ('question', 'answer'),
                          'en': ('question', 'answer')}


translator.register(FaqPage, FaqPageTranslationOptions)
translator.register(Questions, QuestionsTranslationOptions)