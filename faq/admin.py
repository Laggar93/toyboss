from django.contrib import admin
from .models import FaqPage, Questions
from modeltranslation.admin import TranslationAdmin


class FaqPageAdmin(TranslationAdmin):
    model = FaqPage
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class QuestionsAdmin(TranslationAdmin):
    model = Questions
    save_on_top = True


admin.site.register(FaqPage, FaqPageAdmin)
admin.site.register(Questions, QuestionsAdmin)
