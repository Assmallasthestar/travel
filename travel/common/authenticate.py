# 自定义用户登录的认证


from django.contrib.auth.backends import ModelBackend
from rest_framework import serializers
from wx.models import WxUser
from django.db.models import Q


class MyBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = WxUser.objects.get(Q(username=username) | Q(email=username))
        except:
            raise serializers.ValidationError({'error': "未找到该用户！"})
        else:
            # 验证密码是否正确
            if user.check_password(password):
                return user
            else:
                raise serializers.ValidationError({'error': "密码错误！"})
