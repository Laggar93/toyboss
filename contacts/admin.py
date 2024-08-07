from django.contrib import admin
from .models import ContactsPage, SocialNetwork, SocialItems, Schedule, MarketingDepartment, \
    ProductionDepartment, Accounting, CentralOffice, CorporateOffice, ContactForm
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


class ContactsPageAdmin(TranslationAdmin):
    model = ContactsPage
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class SocialItemsAdmin(admin.StackedInline):
    model = SocialItems
    extra = 0
    max_num = 4


class SocialNetworkAdmin(TranslationAdmin):
    model = SocialNetwork
    inlines = [SocialItemsAdmin]
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class ScheduleAdmin(TranslationAdmin):
    model = Schedule
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class MarketingDepartmentAdmin(TranslationAdmin):
    model = MarketingDepartment
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class ProductionDepartmentAdmin(TranslationAdmin):
    model = ProductionDepartment
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class AccountingAdmin(TranslationAdmin):
    model = Accounting
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class CentralOfficeAdmin(TranslationAdmin):
    model = CentralOffice
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class CorporateOfficeAdmin(TranslationAdmin):
    model = CorporateOffice
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class ContactFormAdmin(TranslationAdmin):
    model = ContactForm
    save_on_top = True


admin.site.register(ContactsPage, ContactsPageAdmin)
admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(MarketingDepartment, MarketingDepartmentAdmin)
admin.site.register(ProductionDepartment, ProductionDepartmentAdmin)
admin.site.register(Accounting, AccountingAdmin)
admin.site.register(CentralOffice, CentralOfficeAdmin)
admin.site.register(CorporateOffice, CorporateOfficeAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
