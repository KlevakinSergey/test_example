from django.contrib import admin
from .models import Application, SiteSettings, Layout


class SingletonModelAdmin(admin.ModelAdmin):
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    pass


admin.site.register(Application)
admin.site.register(Layout)


