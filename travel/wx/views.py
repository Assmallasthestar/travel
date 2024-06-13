import os.path
import re

from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
import json
import logging

from django.forms import model_to_dict

from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from weixin import WXAPPAPI
from weixin.oauth2 import OAuth2AuthExchangeError

from travel.settings import MEDIA_ROOT
from wx.permission import UserPermission
from wx.serializers import *

logger = logging.getLogger('django')


def create_or_update_user_info(openid, user_info):
    """
    创建或者更新用户信息
    :param openid: 微信 openid
    :param user_info: 微信用户信息
    :return: 返回用户对象
    """
    if openid:
        if user_info:
            # 创建或更新对象
            user, created = WxUser.objects.update_or_create(openid=openid, defaults=user_info)
        else:
            # 查找或创建对象
            user, created = WxUser.objects.get_or_create(openid=openid)
        return user
    return None


# 邮箱,用户名登陆
class Login(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        # 自定义登录成功后返回的结果
        result = serializer.validated_data
        result['id'] = serializer.user.id
        result['email'] = serializer.user.email
        result['username'] = serializer.user.username
        result['token'] = result.pop('access')
        return Response(result, status=status.HTTP_200_OK)


# 微信登录
class WxLoginView(APIView):
    """
    post:
    微信登录接口
    """
    authentication_classes = []
    permission_classes = []
    fields = {
        'nick_name': 'nickName',
        'gender': 'gender',
        'language': 'language',
        'city': 'city',
        'province': 'province',
        'country': 'country',
        'avatar_url': 'avatarUrl',
    }

    def post(self, request):
        user_info = dict()
        code = request.data.get('code')
        logger.info("Code: {0}".format(code))
        user_info_raw = request.data.get('user_info', {})
        if isinstance(user_info_raw, str):
            user_info_raw = json.loads(user_info_raw)
        if not isinstance(user_info_raw, dict):
            user_info_raw = {}
        # 日志
        logger.info("user_info: {0}".format(user_info_raw))
        if code:
            api = WXAPPAPI(appid=settings.WX_APP_ID, app_secret=settings.WX_APP_SECRET)
            try:
                # 获取open_id和session_key
                session_info = api.exchange_code_for_session_key(code=code)
            except OAuth2AuthExchangeError:
                session_info = None
            if session_info:
                openid = session_info.get('openid', None)
                if openid:
                    if user_info_raw:
                        for k, v in self.fields.items():
                            user_info[k] = user_info_raw.get(v)
                    user = create_or_update_user_info(openid, user_info)
                    if user:
                        token = JfwTokenObtainPairSerializer.get_token(user).access_token
                        return Response(
                            {
                                'token': str(token),
                                # 指定返回字段
                                'user': model_to_dict(
                                    user,
                                    fields=[
                                        'id', 'username', 'email'
                                    ])
                            },
                            status=HTTP_200_OK)
        return Response({'jwt': None, 'user': {}}, status=HTTP_204_NO_CONTENT)


# 获取用户信息   用户相关操作视图集
class UserView(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = WxUser.objects.all()
    serializer_class = WxUserSerializer
    # 设置认证用户才能访问
    permission_classes = [IsAuthenticated, UserPermission]

    def upload_avatar(self, request, *args, **kwargs):
        # 上传用户头像
        avatar = request.data.get('avatar')
        # 校验是否上传文件
        if not avatar:
            return Response({'error': '上传失败，文件不能为空'},  status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 校验文件大小不能超过300kb
        if avatar.size > 1024 * 300:
            return Response({'error': '上传失败，文件大小不能超过300kb'},  status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 保存文件
        user = self.get_object()
        # 获取序列化对象
        ser = self.get_serializer(user, data={"avatar": avatar}, partial=True)
        # 校验
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'url': ser.data['avatar']})

    def update_nickname(self, request, *args, **kwargs):
        # 修改用户昵称

        # 获取参数
        nick_name = request.data.get('nick_name')
        # 校验参数
        if not nick_name:
            return Response({'error': "昵称不能为空"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 修改用户昵称
        user = self.get_object()
        user.nick_name = nick_name
        user.save()
        return Response({'message': "修改用户昵称成功"}, status=status.HTTP_200_OK)

    def update_gender(self, request, *args, **kwargs):
        # 修改用户性别

        # 获取参数
        gender = request.data.get('gender')
        # 校验参数
        if not gender:
            return Response({'error': "性别不能为空"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 修改用户昵称
        user = self.get_object()
        user.gender = gender
        user.save()
        return Response({'message': "修改用户性别成功"}, status=status.HTTP_200_OK)

    def update_email(self, request, *args, **kwargs):
        # 修改用户邮箱
        # 获取参数
        email = request.data.get('email')
        user = self.get_object()
        # 校验参数
        # 参数不能为空
        if not email:
            return Response({'error': "邮箱不能为空"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 邮箱格式是否正确
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            return Response({'error': "邮箱格式有误"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 邮箱地址和之前是否一样
        if user.email == email:
            return Response({'error': "修改的邮箱地址不能和原邮箱地址一样"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 是否被其他用户绑定
        if WxUser.objects.filter(email=email).exists():
            return Response({'error': "该邮箱已被其他用户绑定"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 修改邮箱
        user.email = email
        user.save()
        return Response({'message': "修改邮箱成功"}, status=status.HTTP_200_OK)

    def update_password(self, request, *args, **kwargs):
        # 修改密码
        user = self.get_object()
        # 获取参数
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        # 校验参数
        if not password:
            return Response({'error': "密码不能为空"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if not password_confirmation:
            return Response({'error': "确认密码不能为空"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if password != password_confirmation:
            return Response({'error': "两次密码输入不一致"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 修改密码
        user.set_password(password)
        user.save()

        return Response({'message': "修改密码成功"}, status=status.HTTP_200_OK)


class FileView(APIView):

    def get(self, requests, name):
        path = MEDIA_ROOT / name
        if os.path.isfile(path):
            return FileResponse(open(path, 'rb'))
        return Response({'code': "没有找到改文件！"}, status=status.HTTP_404_NOT_FOUND)


class FeedbackView(GenericViewSet, mixins.CreateModelMixin):
    # 用户反馈
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # 设置认证用户才能访问
    permission_classes = [IsAuthenticated, UserPermission]

    def create(self, request, *args, **kwargs):
        # 获取请求参数
        content = request.data.get('content')
        # 校验参数
        if not content:
            return Response({'error': "反馈不能为空"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 调用继承过来的方法进行创建
        return super().create(request, *args, **kwargs)
