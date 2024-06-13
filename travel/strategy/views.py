import http

from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from strategy.models import Strategy, Collect, Like, Comment
from strategy.permission import StrategyPermission
from strategy.serializers import CollectSerializer, LikeSerializer, CommentSerializer, StrategyListSerializer, \
    StrategyDetailSerializer, CommentListSerializer
from wx.models import WxUser


# Create your views here.
class IndexView(APIView):

    def get(self, request):
        # 获取推荐列表
        strategy = Strategy.objects.all()
        strategy_ser = StrategyListSerializer(strategy, many=True, context={'request': request})
        result = dict(
            strategy=strategy_ser.data
        )
        return Response(result)


# 攻略视图集
class StrategyView(ReadOnlyModelViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategyDetailSerializer


class CollectView(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    # 收藏攻略视图集
    # create: 收藏攻略
    # delete：取消收藏
    # list：收藏攻略列表接口

    queryset = Collect.objects.all()
    serializer_class = CollectSerializer

    # 设置认证用户才能访问
    permission_classes = [IsAuthenticated]

    def get_collect(self, request):
        # 获取当前用户是否收藏攻略
        params_user_id = request.query_params.get('user')
        params_strategy_id = request.query_params.get('strategy')
        is_collect = Collect.objects.filter(user__id=params_user_id, strategy__id=params_strategy_id)
        if not is_collect:
            return Response(status=status.HTTP_404_NOT_FOUND)
        collect_ser = self.get_serializer(is_collect, many=True)
        result = dict(collect=collect_ser.data)
        return Response(result, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        # 收藏攻略
        # 获取请求参数
        user = request.user
        params_user_id = request.data.get('user')
        params_strategy_id = request.data.get('strategy')
        is_collect = Collect.objects.filter(user__id=params_user_id, strategy__id=params_strategy_id)
        if is_collect:
            return Response({'error': "该收藏已经创建"})
        # 校验请求参数中的用户id是否为当前登录的用户
        if user.id != params_user_id:
            return Response({'error': "没有操作其他用户的权限！"})
        # 调用继承过来的方法进行创建
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # 获取用户收藏列表
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_my_collect(self, request, *args, **kwargs):
        # 获取我的推荐列表
        user = request.user
        collect = Collect.objects.filter(user__id=user.id)
        result = []
        for obj in collect:
            strategy = Strategy.objects.filter(id=obj.strategy_id)
            # 序列化如果有图片字段，返回数据需要补全完整的图片获取域名，需要在序列化时传入请求对象。
            collect_ser = StrategyListSerializer(strategy, many=True, context={'request': request})
            result += collect_ser.data
        return Response(result, status=status.HTTP_200_OK)


class LikeView(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    # 点赞攻略视图集
    # create: 点赞攻略
    # delete：取消点赞
    # list：点赞攻略列表接口

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    # 设置认证用户才能访问
    permission_classes = [IsAuthenticated]

    def get_like(self, request):
        # 获取当前用户是否点赞攻略
        params_user_id = request.query_params.get('user')
        params_strategy_id = request.query_params.get('strategy')
        is_like = Like.objects.filter(user__id=params_user_id, strategy__id=params_strategy_id)
        if not is_like:
            return Response(status=status.HTTP_404_NOT_FOUND)
        like_ser = self.get_serializer(is_like, many=True)
        result = dict(like=like_ser.data)
        return Response(result, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        # 点赞攻略
        # 获取请求参数
        user = request.user
        params_user_id = request.data.get('user')
        params_strategy_id = request.data.get('strategy')
        is_like = Like.objects.filter(user__id=params_user_id, strategy__id=params_strategy_id)
        if is_like:
            return Response({'error': "该收藏已经创建"})
        # 校验请求参数中的用户id是否为当前登录的用户
        if user.id != params_user_id:
            return Response({'error': "没有操作其他用户的权限！"})
        # 调用继承过来的方法进行创建
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # 获取用户点赞列表
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentView(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    # 评论攻略视图集
    # create: 评论攻略
    # delete：删除评论
    # list：评论攻略列表接口
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # 设置认证用户才能访问
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # 评论攻略
        # 获取请求参数
        comment = request.data.get('comment')
        user = request.user
        params_user_id = request.data.get('user')
        # 校验评论是否超过长度
        # if len(comment) > 1000:
        #     return Response({'error': "评论字数过长！"})
        # 校验请求参数中的用户id是否为当前登录的用户
        if user.id != params_user_id:
            return Response({'error': "没有操作其他用户的权限！"})
        # 调用继承过来的方法进行创建
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # 获取用户点赞列表
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 攻略评论区列表
class StrategyCommentView(ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    # 实现通过推荐分类进行过滤
    filterset_fields = ('strategy',)
    # 实现通过评分和创建时间排序
    ordering_fields = 'create_time'
