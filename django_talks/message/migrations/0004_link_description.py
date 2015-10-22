# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_remove_link_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
