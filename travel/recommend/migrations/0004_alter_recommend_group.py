# Generated by Django 3.2 on 2023-08-06 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_alter_grade_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='group',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='recommend.area', verbose_name='地区分类'),
        ),
    ]