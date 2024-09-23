from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class NavigationMenuAdmin(TranslationAdmin):
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class FooterAdmin(TranslationAdmin):
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class NotFoundAdmin(TranslationAdmin):
    save_on_top = True
    readonly_fields = ('display_image',)
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class GeneralTranslationsAdmin(TranslationAdmin):
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(NavigationMenu, NavigationMenuAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(NotFound, NotFoundAdmin)
admin.site.register(GeneralTranslations, GeneralTranslationsAdmin)
