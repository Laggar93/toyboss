from modeltranslation.translator import translator, TranslationOptions
from .models import *


class ContactsPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'page_title', 'page_subtitle')
    required_languages = {'ky': ('title', 'page_title', 'page_subtitle'),
                          'en': ('title', 'page_title', 'page_subtitle')}


class SocialNetworkTranslationOptions(TranslationOptions):
    fields = ('page_title',)
    required_languages = {'ky': ('page_title',),
                          'en': ('page_title',)}


class ScheduleTranslationOptions(TranslationOptions):
    fields = ('schedule_title', 'monday_friday', 'dinner')
    required_languages = {'ky': ('schedule_title', 'monday_friday', 'dinner'),
                          'en': ('schedule_title', 'monday_friday', 'dinner')}


class MarketingDepartmentTranslationOptions(TranslationOptions):
    fields = ('marketing_department_title',)
    required_languages = {'ky': ('marketing_department_title',),
                          'en': ('marketing_department_title',)}


class ProductionDepartmentTranslationOptions(TranslationOptions):
    fields = ('production_department_title',)
    required_languages = {'ky': ('production_department_title',),
                          'en': ('production_department_title',)}


class AccountingTranslationOptions(TranslationOptions):
    fields = ('accounting_department_title',)
    required_languages = {'ky': ('accounting_department_title',),
                          'en': ('accounting_department_title',)}


class CentralOfficeTranslationOptions(TranslationOptions):
    fields = ('central_office_title', 'central_office_address')
    required_languages = {'ky': ('central_office_title', 'central_office_address'),
                          'en': ('central_office_title', 'central_office_address')}


class CorporateOfficeTranslationOptions(TranslationOptions):
    fields = ('corporate_office_title', 'corporate_office_address')
    required_languages = {'ky': ('corporate_office_title', 'corporate_office_address'),
                          'en': ('corporate_office_title', 'corporate_office_address')}


class ContactFormTranslationOptions(TranslationOptions):
    fields = ('main_title', 'subtitle', 'name', 'email', 'message', 'rules', 'send_button', 'phone')
    required_languages = {'ky': ('main_title', 'subtitle', 'name', 'email', 'message', 'rules', 'send_button', 'phone'),
                          'en': ('main_title', 'subtitle', 'name', 'email', 'message', 'rules', 'send_button', 'phone')}


translator.register(ContactsPage, ContactsPageTranslationOptions)
translator.register(SocialNetwork, SocialNetworkTranslationOptions)
translator.register(Schedule, ScheduleTranslationOptions)
translator.register(MarketingDepartment, MarketingDepartmentTranslationOptions)
translator.register(ProductionDepartment, ProductionDepartmentTranslationOptions)
translator.register(Accounting, AccountingTranslationOptions)
translator.register(CentralOffice, CentralOfficeTranslationOptions)
translator.register(CorporateOffice, CorporateOfficeTranslationOptions)
translator.register(ContactForm, ContactFormTranslationOptions)