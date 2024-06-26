# Generated by Django 3.2 on 2023-08-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0004_alter_recommend_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='rate',
            field=models.SmallIntegerField(choices=[(1, '不推荐'), (2, '推荐'), (0, '非常不推荐'), (3, '非常推荐')], default=2, verbose_name='推荐指数'),
        ),
    ]
