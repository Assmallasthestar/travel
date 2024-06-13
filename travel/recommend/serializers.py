# 推荐模块序列化器
from .models import *
from rest_framework import serializers


# 地区序列化器
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


# 推荐序列化器
class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = "__all__"


# 评分序列化器
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"
