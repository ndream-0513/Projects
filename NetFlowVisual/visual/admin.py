from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin, GroupAdmin

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

# 定制User
class MyUserAdmin(UserAdmin):
    def has_module_permission(self, request):
    # 返回False将在admin中隐藏User模块
        return False

# 定制Group
class MyGroupAdmin(GroupAdmin):
    def has_module_permission(self, request):
    # 返回False将在admin中隐藏Group模块
        return False

# 重新注册User和Group模型以使用上面的定制类
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, MyGroupAdmin)

admin.site.register(LogApp, LogAppAdmin)
admin.site.register(LogDns, LogDnsAdmin)
admin.site.register(LogNetflow, LogNetflowAdmin)

admin.site.site_header = '网络流量分析'
admin.site.site_title = '管理'
admin.site.index_title = ''

