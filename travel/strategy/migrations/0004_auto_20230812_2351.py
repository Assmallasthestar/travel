# Generated by Django 3.2 on 2023-08-12 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0003_alter_comment_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collect',
            options={'verbose_name': '收藏', 'verbose_name_plural': '收藏'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': '点赞', 'verbose_name_plural': '点赞'},
        ),
        migrations.AlterModelOptions(
            name='strategy',
            options={'verbose_name': '攻略', 'verbose_name_plural': '攻略'},
        ),
    ]