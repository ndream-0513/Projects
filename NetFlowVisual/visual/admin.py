from django.contrib import admin

from visual.models import LogApp, LogDns, LogNetflow

admin.site.register(LogApp)
admin.site.register(LogDns)
admin.site.register(LogNetflow)
