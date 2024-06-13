from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


# 自定义令牌
class JfwTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(JfwTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = 'wx_{0}'.format(user.username)
        return token


# user序列化器
class WxUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = WxUser
        fields = ['id', 'username', 'nick_name', 'avatar', 'email', 'gender']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
