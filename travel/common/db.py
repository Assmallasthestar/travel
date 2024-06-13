from django.db import models

class BaseModel(models.Model):
    # 抽象的模型基类：定义一些公共的模型字段
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        # 声明抽象模型，执行迁移文件时，不会在数据中生成表
        abstract = True
        verbose_name_plural = "公共字段模型"
        db_table = 'BaseTable'
