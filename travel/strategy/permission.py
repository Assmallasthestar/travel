from rest_framework import permissions


class StrategyPermission(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    """

    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求，
        # 所以我们总是允许GET，HEAD或OPTIONS请求。
        # 判断是否是超级管理员
        if request.user.is_superuser:
            return True

        # 只有该snippet的所有者才允许写权限。
        return obj == request.user
