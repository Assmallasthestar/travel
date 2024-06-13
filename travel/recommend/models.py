from django.db import models

# Create your models here.
from common.db import BaseModel


class Area(models.Model):
    # 省市区地址模型
    pid = models.IntegerField(verbose_name='父级的行政区域id')
    name = models.CharField(verbose_name='地区名', max_length=20)
    level = models.CharField(verbose_name='区域等级', max_length=20)
    # 1:省 2：市

    class Meta:
        db_table = 'Area'
        verbose_name = '地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name


# on_delete = models.CASCADE删除关联数据的时候，与之的关联也删除
# on_delete = models.DO_NOTHING删除关联数据的时候，什么操作也不做
# on_delete = models.PROTRCT删除关联数据的时候，引发报错
# on_delete = models.SET_NULL删除关联数据的时候，与之关联的只设置为空
# on_delete = models.SET_DEFAULT删除关联数据的时候，与之关联的只设置为默认值
# on_delete = models.SET删除关联数据
class Recommend(BaseModel, models.Model):
    name = models.CharField(verbose_name='名称', max_length=100, default='')
    img = models.ImageField(verbose_name='图片', default='', null=True, blank=True)
    desc = models.CharField(verbose_name='描述', max_length=200, default='', null=True, blank=True)
    group = models.ForeignKey('Area', on_delete=models.CASCADE, verbose_name='地区分类', max_length=30)
    sort = models.SmallIntegerField(
        verbose_name='推荐类别', choices=((1, '美食'), (2, '景点'), (0, '住宿')), default=2)
    rate = models.SmallIntegerField(
        verbose_name='推荐指数', choices=((2, '不推荐'), (3, '推荐'), (1, '非常不推荐'), (4, '非常推荐'), (5, '极其推荐')), default=2)

    class Meta:
        db_table = 'recommend'
        verbose_name = '推荐'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name


class Grade(BaseModel, models.Model):
    rate = models.SmallIntegerField(
        verbose_name='推荐指数',  choices=((1, '不推荐'), (2, '推荐'), (0, '非常不推荐'), (3, '非常推荐'), (4, '极力推荐')), default=2)
    user = models.ForeignKey('wx.WxUser', on_delete=models.CASCADE)
    recommend = models.ForeignKey('recommend', on_delete=models.CASCADE)

    class Meta:
        db_table = 'grade'
        verbose_name = '评分'
        verbose_name_plural = verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        name = self.user.username + ' ' + self.recommend.name
        return name

