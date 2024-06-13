# Generated by Django 3.2 on 2023-08-05 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ImageField(upload_to='', verbose_name='上级id')),
                ('name', models.CharField(max_length=20, verbose_name='地区名')),
                ('level', models.CharField(max_length=20, verbose_name='区域等级')),
            ],
            options={
                'verbose_name': '地区',
                'db_table': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('img', models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='图片')),
                ('desc', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='描述')),
                ('rate', models.SmallIntegerField(choices=[(1, '不推荐'), (2, '推荐'), (0, '非常不推荐'), (3, '非常推荐'), (4, '极力推荐')], default=2, verbose_name='推荐指数')),
                ('group', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='recommend.area', verbose_name='分类')),
            ],
            options={
                'verbose_name': '推荐',
                'db_table': 'recommend',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('rate', models.SmallIntegerField(choices=[(1, '不推荐'), (2, '推荐'), (0, '非常不推荐'), (3, '非常推荐'), (4, '极力推荐')], default=2, verbose_name='推荐指数')),
                ('recommend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend.recommend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '公共字段模型',
                'db_table': 'BaseTable',
                'abstract': False,
            },
        ),
    ]