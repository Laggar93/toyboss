from django.contrib import admin
from .models import NewsPage, NewsItem, NewsSlider
from modeltranslation.admin import TranslationAdmin


class NewsPageAdmin(TranslationAdmin):
    model = NewsPage
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class NewsSliderAdmin(admin.StackedInline):
    model = NewsSlider
    readonly_fields = ('display_image',)
    extra = 0
    exclude = ('image_1499_webp', 'image_1499_jpg', 'image_main_jpg')


class NewsItemPage(TranslationAdmin):
    model = NewsItem
    inlines = [NewsSliderAdmin]
    save_on_top = True


admin.site.register(NewsPage, NewsPageAdmin)
admin.site.register(NewsItem, NewsItemPage)
