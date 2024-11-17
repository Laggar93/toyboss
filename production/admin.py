from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import ProductionPage, Points, PointsSlider, Advantages
from modeltranslation.admin import TranslationAdmin


class ProductionPageAdmin(TranslationAdmin):
    model = ProductionPage
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class AdvantagesAdmin(TranslationAdmin):
    model = Advantages
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class PointsSliderAdmin(admin.StackedInline):
    model = PointsSlider
    readonly_fields = ('display_image',)
    extra = 0
    exclude = ('image_1470_webp', 'image_1470_jpg', 'image_735_webp', 'image_735_jpg')


class PointsAdmin(SortableAdminMixin, TranslationAdmin):
    model = Points
    save_on_top = True
    inlines = [PointsSliderAdmin]
    ordering = ('order',)


admin.site.register(ProductionPage, ProductionPageAdmin)
admin.site.register(Advantages, AdvantagesAdmin)
admin.site.register(Points, PointsAdmin)

