from django.contrib import admin

from visual.models import LogApp, LogDns, LogNetflow

from .models import LogApp

class LogAppAdmin(admin.ModelAdmin):
    # Custom admin list view
    list_display = ('client_mac', 'app_name', 'start_time', 'end_time', 'host', )
    # list_display_links = ('title', ) # default
    # sortable_by # a sub set of list_display. All fields are sortable by default.

    '''10 items per page'''
    list_per_page = 5

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default

    '''Calling select related objects to reduce SQL queries'''
    #list_select_related = ('client_mac', )

    '''Render a search box at top. ^, =, @, None=icontains'''
    #search_fields = ['client_mac']

    '''Render date options at top. do not accept tuple'''
    #date_hierarchy = 'create_date'

    '''Replacement value for empty field'''
    empty_value_display = 'NA'

    '''filter options'''
    #list_filter = ('status', 'author__is_superuser', )

admin.site.register(LogApp, LogAppAdmin)

admin.site.register(LogDns)
admin.site.register(LogNetflow)

admin.site.site_header = '网络流量分析'
admin.site.site_title = '管理'
admin.site.index_title = ''

