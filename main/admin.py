from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import MainCooperation, MainPage, Groups, MainProd, MainProdSlider, MainPageSlider, MainQuote
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


class MainPageSliderAdmin(SortableAdminMixin, TranslationAdmin):
    model = MainPageSlider
    # ordering = ('order',)
    save_on_top = True
    list_display = ('title', 'image_tag')


class MainPageAdmin(TranslationAdmin):
    model = MainPage
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class MainCooperationAdmin(TranslationAdmin):
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class GroupsAdmin(TranslationAdmin):
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class MainProdSliderAdmin(admin.StackedInline):
    model = MainProdSlider
    extra = 0


class MainProdAdmin(TranslationAdmin):
    model = MainProd
    save_on_top = True
    inlines = [MainProdSliderAdmin]


class MainQuoteAdmin(TranslationAdmin):
    model = MainQuote
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(MainCooperation, MainCooperationAdmin)
admin.site.register(MainPage, MainPageAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(MainProd, MainProdAdmin)
admin.site.register(MainQuote, MainQuoteAdmin)
admin.site.register(MainPageSlider, MainPageSliderAdmin)
