from django.contrib import admin, auth
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
from .models import AboutPage, History, Years, Mission, Vision, Value, ValuePoints, \
    StatisticPoints, Certificates, CertificatesItems, Rewards, RewardsItems, Statistic
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


class AboutPageAdmin(TranslationAdmin):
    model = AboutPage
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class HistoryAdmin(TranslationAdmin):
    model = History
    save_on_top = True
    readonly_fields = ('display_image',)
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class YearsAdmin(TranslationAdmin):
    save_on_top = True
    model = Years


class MissionAdmin(TranslationAdmin):
    model = Mission
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class VisionAdmin(TranslationAdmin):
    model = Vision
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class ValueAdmin(TranslationAdmin):
    model = Value
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class ValuePointsAdmin(TranslationAdmin):
    model = ValuePoints
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class StatisticPointsAdmin(TranslationAdmin):
    model = StatisticPoints
    save_on_top = True


class CertificatesItemsAdmin(TranslationStackedInline):
    model = CertificatesItems
    extra = 0
    readonly_fields = ('display_image',)
    exclude = ('cert_image_184',)


class CertificatesAdmin(TranslationAdmin):
    inlines = [CertificatesItemsAdmin]
    model = Certificates
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class RewardsItemsAdmin(admin.StackedInline):
    model = RewardsItems
    extra = 0
    readonly_fields = ('display_image',)


class RewardsAdmin(TranslationAdmin):
    inlines = [RewardsItemsAdmin]
    model = Rewards
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class StatisticAdmin(TranslationAdmin):
    model = Statistic
    save_on_top = True
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Years, YearsAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(ValuePoints, ValuePointsAdmin)
admin.site.register(StatisticPoints, StatisticPointsAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(Rewards, RewardsAdmin)
admin.site.register(Statistic, StatisticAdmin)
