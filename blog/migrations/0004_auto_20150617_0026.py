# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogindexpage_blogindexrelatedlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
