# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20151022_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='description',
        ),
    ]
