# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0003_auto_20151119_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='schoolslug',
            field=models.SlugField(default=datetime.datetime(2015, 11, 19, 18, 30, 36, 372003, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
