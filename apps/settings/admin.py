from django.contrib import admin
from apps.settings import models
from django.contrib.auth.models import User, Group
from apps.secondary.models import About, Team
from apps.contact.models import Contact
# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'disc')
    search_fields = ('title', 'disc')
class ClientFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'disc')
    search_fields = ('name', 'disc')

admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.Subject)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(models.Partners)
admin.site.register(models.Client, ClientFilterAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
