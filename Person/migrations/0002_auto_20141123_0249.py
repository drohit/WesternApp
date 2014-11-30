# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='courses',
            field=models.ManyToManyField(to='Course.Course', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='residence',
            field=models.CharField(max_length=28, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
