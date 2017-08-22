# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eid_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authenticationrequest',
            name='accessToken',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='authenticationrequest',
            name='openidParameter',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authenticationrequest',
            name='restrictedId',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
    ]
