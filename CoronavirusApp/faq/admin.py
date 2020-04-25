from django.contrib import admin
from .models import Articles

admin.sites.site.register(Articles)


