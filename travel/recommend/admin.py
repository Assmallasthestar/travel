from django.contrib import admin
from recommend.models import *
# Register your models here.


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    search_fields = ['name', 'level']


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    search_fields = ['name', 'group__name', 'sort', 'rate']
    # 只读字段
    readonly_fields = (
        'create_time', 'update_time', 'rate'
    )


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'recommend__name', 'rate']
    # 只读字段
    readonly_fields = (
        'create_time', 'update_time', 'rate', 'user', 'recommend'
    )
