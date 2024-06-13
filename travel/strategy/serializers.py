# 攻略模块序列化器
from wx.serializers import WxUserSerializer
from .models import *
from rest_framework import serializers


# 攻略列表序列化器
class StrategyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['id', 'title', 'img', 'desc', 'user', 'area']


# 攻略详情序列化器
class StrategyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = "__all__"


# 评论序列化器
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


# 评论列表序列化器
class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


# 点赞序列化器
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


# 收藏序列化器
class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = "__all__"
