# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0004_school_schoolslug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='schoolid',
        ),
    ]
