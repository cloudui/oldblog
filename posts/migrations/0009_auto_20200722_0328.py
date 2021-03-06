# Generated by Django 3.0.8 on 2020-07-22 07:28

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200629_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
