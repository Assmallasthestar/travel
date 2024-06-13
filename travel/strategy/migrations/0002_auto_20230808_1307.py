# Generated by Django 3.2 on 2023-08-08 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0007_alter_area_pid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategy',
            name='name',
        ),
        migrations.AddField(
            model_name='strategy',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wx.wxuser', verbose_name='作者'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='strategy',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend.area', verbose_name='地区分类'),
        ),
    ]