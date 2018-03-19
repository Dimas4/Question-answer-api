# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('glavapp', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='answer',
            field=models.TextField(default=datetime.datetime(2018, 3, 19, 6, 33, 45, 706906, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
