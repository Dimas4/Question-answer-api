# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glavapp', '0004_message_data_new'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
