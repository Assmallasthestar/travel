# Generated by Django 3.2 on 2023-08-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0002_auto_20230808_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=1000, verbose_name='内容'),
        ),
    ]