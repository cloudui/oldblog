# Generated by Django 3.0.8 on 2021-02-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210203_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]