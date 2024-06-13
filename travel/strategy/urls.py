from django.urls import path, re_path
from .views import *

urlpatterns = [
    # 推荐页面数据获取
    path('index/', IndexView.as_view()),
    # 获取单个攻略数据
    path('strategy/<int:pk>/', StrategyView.as_view({"get": "retrieve"})),
    # 收藏攻略和获取收藏列表
    path('collect/', CollectView.as_view({"post": "create", "get": "list"})),
    # 取消收藏
    path('collect/<int:pk>/', CollectView.as_view({"delete": "destroy"})),
    # 用户是否收藏某攻略
    path('isCollect/', CollectView.as_view({"get": "get_collect"})),
    # 点赞攻略和获取点赞列表
    path('like/', LikeView.as_view({"post": "create", "get": "list"})),
    # 取消点赞
    path('like/<int:pk>/', LikeView.as_view({"delete": "destroy"})),
    # 用户是否点赞某攻略
    path('isLike/', LikeView.as_view({"get": "get_like"})),
    # 评论攻略和获取我的评论列表
    path('comment/', CommentView.as_view({"post": "create", "get": "list"})),
    # 删除评论
    path('comment/<int:pk>/', CommentView.as_view({"delete": "destroy"})),
    # 攻略评论区列表
    path('strategy/comment/', StrategyCommentView.as_view({"get": "list"})),
    # 我的收藏列表
    path('myCollect/<int:pk>/', CollectView.as_view({"get": "get_my_collect"})),
]
