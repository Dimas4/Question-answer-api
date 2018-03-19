# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('glavapp', '0003_remove_message_data_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='data_new',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 18, 19, 37, 28, 423874, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
