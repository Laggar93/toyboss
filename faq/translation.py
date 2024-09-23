from modeltranslation.translator import translator, TranslationOptions
from .models import *


class FaqPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title', 'main_button')
    required_languages = {'ky': ('title', 'page_title', 'main_button'),
                          'en': ('title', 'page_title', 'main_button')}


class QuestionsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
    required_languages = {'ky': ('question', 'answer'),
                          'en': ('question', 'answer')}


translator.register(FaqPage, FaqPageTranslationOptions)
translator.register(Questions, QuestionsTranslationOptions)