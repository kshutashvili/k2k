# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-04-04 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='theme',
            field=models.CharField(choices=[('credit', '\u041a\u0440\u0435\u0434\u0438\u0442'), ('transfers', '\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b')], default='credit', max_length=20, verbose_name='\u0422\u0435\u043c\u0430'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('phone', '\u0422\u0435\u043b\u0435\u0444\u043e\u043d'), ('email', '\u041f\u043e\u0447\u0442\u0430'), ('telegram', '\u0422\u0435\u043b\u0435\u0433\u0440\u0430\u043c')], max_length=20, verbose_name='\u0422\u0438\u043f'),
        ),
    ]
