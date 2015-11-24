# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0009_auto_20151123_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='nesascores',
            name='grade',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
