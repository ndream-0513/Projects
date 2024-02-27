from django.contrib import admin

from visual.models import LogApp, LogDns, LogNetflow

from .models import LogApp

class LogAppAdmin(admin.ModelAdmin):
    # Custom admin list view
    list_display = ('client_mac', 'app_name', 'readable_start_time', 'readable_end_time', 'host', )

    search_fields = ('client_mac', 'app_name', 'host', )

    readonly_fields = ('start_time', 'end_time', )

    '''10 items per page'''
    list_per_page = 10

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default

    '''Replacement value for empty field'''
    empty_value_display = 'NA'

class LogDnsAdmin(admin.ModelAdmin):
    # Custom admin list view
    list_display = ('type', 'client_mac', 'domain', 'rdata', 'readable_time', )

    search_fields = ('type', 'client_mac', 'domain', 'rdata', )

    '''10 items per page'''
    list_per_page = 10

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default

    '''Replacement value for empty field'''
    empty_value_display = 'NA'

class LogNetflowAdmin(admin.ModelAdmin):
    # Custom admin list view
    list_display = ('client_mac', 'ip_src', 'ip_dst', 'port_src', 'port_dst', 'readable_time_start', 'readable_time_end', 'len', 'type', 'host', )

    search_fields = ('client_mac', 'ip_src', 'ip_dst', 'port_src', 'port_dst', 'len', 'type', 'host', )

    '''10 items per page'''
    list_per_page = 10

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default

    '''Replacement value for empty field'''
    empty_value_display = 'NA'

admin.site.register(LogApp, LogAppAdmin)
admin.site.register(LogDns, LogDnsAdmin)
admin.site.register(LogNetflow, LogNetflowAdmin)

admin.site.site_header = '网络流量分析'
admin.site.site_title = '管理'
admin.site.index_title = ''

