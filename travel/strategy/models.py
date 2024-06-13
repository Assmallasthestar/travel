from django.db import models
from common.db import BaseModel
# Create your models here.
from ckeditor.fields import RichTextField


class Strategy(BaseModel, models.Model):
    title = models.CharField(verbose_name='标题', max_length=200, default='', null=True, blank=True)
    img = models.ImageField(verbose_name='封面', default='', null=True, blank=True)
    desc = models.CharField(verbose_name='描述', max_length=200, default='', null=True, blank=True)
    content = RichTextField(verbose_name='内容')
    user = models.ForeignKey('wx.WxUser', on_delete=models.CASCADE, verbose_name='作者')
    area = models.ForeignKey('recommend.Area', on_delete=models.CASCADE, verbose_name='地区分类')

    class Meta:
        db_table = 'strategy'
        verbose_name = '攻略'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.title


class Comment(BaseModel, models.Model):
    user = models.ForeignKey('wx.WxUser', on_delete=models.CASCADE, verbose_name='所属用户', related_name='user_info')
    strategy = models.ForeignKey('Strategy', on_delete=models.CASCADE, verbose_name='所属攻略')
    content = models.CharField(verbose_name='内容', max_length=1000)

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.user.username + ' ' + self.strategy.title


class Like(BaseModel, models.Model):
    user = models.ForeignKey('wx.WxUser', on_delete=models.CASCADE, verbose_name='所属用户')
    strategy = models.ForeignKey('Strategy', on_delete=models.CASCADE, verbose_name='所属攻略')

    class Meta:
        db_table = 'like'
        verbose_name = '点赞'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.user.username + ' ' + self.strategy.title


class Collect(BaseModel, models.Model):
    user = models.ForeignKey('wx.WxUser', on_delete=models.CASCADE, verbose_name='所属用户')
    strategy = models.ForeignKey('Strategy', on_delete=models.CASCADE, verbose_name='所属攻略')

    class Meta:
        db_table = 'collect'
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.user.username + ' ' + self.strategy.title
