from django.contrib import admin
from .models import Support, Group, Activity

class SupportAdmin(admin.ModelAdmin):
    search_fields = ['name','undergrad']

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name','undergrad']

class ActivityAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'undergrad']

admin.site.register(Support, SupportAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Activity, ActivityAdmin)