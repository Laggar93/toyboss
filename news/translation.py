from modeltranslation.translator import translator, TranslationOptions
from .models import *


class NewsPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title', 'other_news_title', 'button_name')
    required_languages = {'ky': ('title', 'page_title', 'other_news_title', 'button_name'),
                          'en': ('title', 'page_title', 'other_news_title', 'button_name')}


class NewsItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'news_title', 'text')
    required_languages = {'ky': ('title', 'news_title', 'text'),
                          'en': ('title', 'news_title', 'text')}


translator.register(NewsPage, NewsPageTranslationOptions)
translator.register(NewsItem, NewsItemTranslationOptions)