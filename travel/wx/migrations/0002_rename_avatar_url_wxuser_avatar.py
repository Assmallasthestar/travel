# Generated by Django 3.2 on 2023-08-09 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wxuser',
            old_name='avatar_url',
            new_name='avatar',
        ),
    ]
