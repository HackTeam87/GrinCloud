# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170611_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='med/', verbose_name='Ваше фото'),
        ),
    ]