# Generated by Django 3.2 on 2023-08-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0007_alter_area_pid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': '地区', 'verbose_name_plural': '地区'},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': '评分', 'verbose_name_plural': '评分'},
        ),
        migrations.AlterModelOptions(
            name='recommend',
            options={'verbose_name': '推荐', 'verbose_name_plural': '推荐'},
        ),
        migrations.AlterField(
            model_name='area',
            name='pid',
            field=models.IntegerField(verbose_name='父级的行政区域id'),
        ),
    ]
