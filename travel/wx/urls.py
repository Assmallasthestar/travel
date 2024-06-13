from django.urls import re_path, path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from wx.apps import WxConfig

from .views import *


API_TITLE = 'API Documents'
API_DESCRIPTION = 'API Information'

app_name = WxConfig.name


urlpatterns = format_suffix_patterns([
    # 普通登录
    path('login/', Login.as_view()),
    # 微信登录
    re_path(r'^wx_login/$', WxLoginView.as_view(), name='wx_login'),
    # 刷新token
    path('token/refresh/', TokenRefreshView.as_view()),
    # 校验token
    path('token/verify/', TokenVerifyView.as_view()),
    # 获取单个用户信息的路由
    path('users/<int:pk>/', UserView.as_view({'get': 'retrieve'})),
    # 上传用户头像的接口
    path('<int:pk>/avatar/upload', UserView.as_view({"post": "upload_avatar"})),
    # 修改用户昵称
    path('<int:pk>/name/', UserView.as_view({"put": "update_nickname"})),
    # 修改用户性别
    path('<int:pk>/gender/', UserView.as_view({"put": "update_gender"})),
    # 修改邮箱
    path('<int:pk>/email/', UserView.as_view({"put": "update_email"})),
    # 修改密码
    path('<int:pk>/password/', UserView.as_view({"put": "update_password"})),
    # 用户反馈
    path('feedback/', FeedbackView.as_view({"put": "create"})),
])
