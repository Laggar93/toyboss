from django.contrib import admin
from .models import CooperationPage, Wholesale, Retailsale, Partners, PartnersItems, CooperationForm
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


class CooperationPageAdmin(TranslationAdmin):
    model = CooperationPage
    save_on_top = True
    readonly_fields = ('display_image',)
    exclude = ('image_1500_webp', 'image_1500_jpg')
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class WholesaleAdmin(TranslationAdmin):
    model = Wholesale
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class RetailsaleAdmin(TranslationAdmin):
    model = Retailsale
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class PartnersItemsAdmin(admin.StackedInline):
    model = PartnersItems
    readonly_fields = ('display_image',)
    extra = 0


class PartnersAdmin(TranslationAdmin):
    model = Partners
    save_on_top = True
    inlines = [PartnersItemsAdmin]
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class CooperationFormAdmin(TranslationAdmin):
    model = CooperationForm
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(CooperationPage, CooperationPageAdmin)
admin.site.register(Wholesale, WholesaleAdmin)
admin.site.register(Retailsale, RetailsaleAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(CooperationForm, CooperationFormAdmin)
