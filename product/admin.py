from django.contrib import admin
from .models import ProductCategory, Products, ProductPage
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


class ProductCategoryAdmin(SortableAdminMixin, TranslationAdmin):
    model = ProductCategory
    ordering = ('order',)


class ProductsAdmin(SortableAdminMixin, TranslationAdmin):
    model = Products
    save_on_top = True
    readonly_fields = ('display_image_semismocked', 'display_image_boiled', 'display_image_chicken', 'display_image_sausages',
                       'display_image_detail', 'display_first_image_animation', 'display_second_image_animation', 'display_third_image_animation')
    ordering = ('order',)
    list_display = ('product_title', 'product', 'main_show', 'image_tag',)
    list_filter = ('product',)


class ProductPageAdmin(admin.ModelAdmin):
    model = ProductPage


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductPage, ProductPageAdmin)

