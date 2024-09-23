from modeltranslation.translator import translator, TranslationOptions
from .models import *


class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('category_title',)
    # required_languages = {'ky': ('category_title'),
    #                       'en': ('category_title')}


class ProductsTranslationOptions(TranslationOptions):
    fields = ('product_title', 'description', 'compound', 'fact')
    # required_languages = {'ky': ('category_title'),
    #                       'en': ('category_title')}


class ProductPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title')
    required_languages = {'ky': ('title', 'page_title'),
                          'en': ('title', 'page_title')}


translator.register(ProductCategory, ProductCategoryTranslationOptions)
translator.register(Products, ProductsTranslationOptions)
translator.register(ProductPage, ProductPageTranslationOptions)


