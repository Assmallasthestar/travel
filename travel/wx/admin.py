from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from wx.models import *

admin.site.site_header = '旅游信息管理后台'  # 设置header
admin.site.site_title = '旅游信息管理后台'   # 设置title
admin.site.index_title = '旅游信息管理后台'


@admin.register(WxUser)
class WxUserAdmin(admin.ModelAdmin):
    # 只读字段
    readonly_fields = (
        'last_login', 'date_joined',
        'create_time', 'update_time'
    )
    # 增加搜索栏
    search_fields = [
        'username', 'email', 'nick_name', 'openid'
        ]
    fieldsets = (
        (_('基础信息'), {'fields': ('username', 'password', 'openid', 'email')}),
        (_('个人信息'), {'fields': (
            'nick_name', 'avatar', 'gender')}),
        (_('登录信息'), {'fields': ('last_login', 'create_time', 'update_time')}),
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # 只读字段
    readonly_fields = (
        'user', 'content',
        'create_time', 'update_time'
    )
    # 搜索
    search_fields = [
        'user__username'
    ]
