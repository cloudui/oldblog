# Generated by Django 3.0.8 on 2021-02-03 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200722_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='caption_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]
