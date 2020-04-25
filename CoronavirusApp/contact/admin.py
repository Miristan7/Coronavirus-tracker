from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'create_at')
    list_filter = ('status', 'create_at')


admin.sites.site.register(Contact, ContactAdmin)