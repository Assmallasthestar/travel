from django.db import models

# Create your models here.
import hashlib

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.db import BaseModel


class WxUser(AbstractUser, BaseModel):
    """
    自定义的用户模块
    """
    # 微信同步的用户信息
    openid = models.CharField(
        verbose_name=_('微信OpenID'), help_text=_('微信OpenID'), max_length=100, unique=True, null=True, blank=True)
    avatar = models.ImageField(
        verbose_name=_('头像'), help_text=_('头像'), null=True, blank=True)
    nick_name = models.CharField(
        verbose_name=_('昵称'), help_text=_('昵称'), max_length=100, null=True, blank=True, unique=True)
    gender = models.SmallIntegerField(
        verbose_name=_('性别'), help_text=_('性别'), choices=((0, '男'), (1, '女'), (2, '未知')), null=True, blank=True)
    language = models.CharField(
        verbose_name=_('语言'), help_text=_('语言'), max_length=100, null=True, blank=True)
    city = models.CharField(
        verbose_name=_('城市'), help_text=_('城市'), max_length=200, null=True, blank=True)
    province = models.CharField(
        verbose_name=_('省份'), help_text=_('省份'), max_length=200, null=True, blank=True)
    country = models.CharField(
        verbose_name=_('国家'), help_text=_('国家'), max_length=200, null=True, blank=True)

    date_of_birth = models.DateField(verbose_name=_('出生日期'), help_text=_('出生日期'), null=True, blank=True)
    desc = models.TextField(verbose_name=_('描述'), help_text=_('描述'), max_length=2000, null=True, blank=True)

    def create_username_password(self):
        if not self.username and not self.password and self.openid:
            key = settings.SECRET_KEY
            self.username = hashlib.pbkdf2_hmac(
                "sha256", getattr(self, 'openid').encode(encoding='utf-8'), key.encode(encoding='utf-8'), 10).hex()
            self.password = hashlib.pbkdf2_hmac(
                "sha256", self.username.encode(), getattr(self, 'openid').encode(encoding='utf-8'), 10).hex()

    def save(self, *args, **kwargs):
        self.create_username_password()
        super().save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Feedback(BaseModel, models.Model):
    user = models.ForeignKey('WxUser', on_delete=models.CASCADE, verbose_name='所属用户')
    content = models.CharField(verbose_name='内容', max_length=1000)

    class Meta:
        db_table = 'feedback'
        verbose_name = '用户反馈'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        result = self.user.username + ' ' + format(self.create_time)
        return result
