# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
        ('blog', '0004_auto_20150617_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='advert',
            field=models.ForeignKey(to='snippets.Advert', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True),
            preserve_default=True,
        ),
    ]
