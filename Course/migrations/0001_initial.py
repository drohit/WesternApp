# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('term', models.CharField(max_length=20)),
                ('title', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
