from django.contrib import admin
from strategy.models import *
# Register your models here.


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    # 只读字段
    readonly_fields = (
        'create_time', 'update_time'
    )
    # 增加搜索栏
    search_fields = [
        'title', 'user__username', 'area__name'
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # 只读字段
    readonly_fields = (
        'create_time', 'update_time', 'user', 'strategy', 'content'
    )
    # 增加搜索栏
    search_fields = [
        'user__username', 'strategy__title'
    ]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # 只读字段
    readonly_fields = (
        'create_time', 'update_time', 'user', 'strategy'
    )
    # 增加搜索栏
    search_fields = [
        'user__username', 'strategy__title'
    ]


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    # 只读字段
    readonly_fields = (
        'create_time', 'update_time', 'user', 'strategy'
    )
    # 增加搜索栏
    search_fields = [
        'user__username', 'strategy__title'
    ]
