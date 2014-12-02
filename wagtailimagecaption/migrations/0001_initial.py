# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0004_make_focal_point_key_not_nullable'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCaption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=255)),
                ('image', models.ForeignKey(related_name='imagecaption', null=True, blank=True, to='wagtailimages.Image', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
