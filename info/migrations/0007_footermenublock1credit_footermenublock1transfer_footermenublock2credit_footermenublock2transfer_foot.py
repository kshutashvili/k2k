# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-04-10 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20180406_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterMenuBlock1Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Flatpage', verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041a\u0440\u0435\u0434\u0438\u0442(\u0411\u043b\u043e\u043a 1)',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041a\u0440\u0435\u0434\u0438\u0442 (\u0411\u043b\u043e\u043a 1)',
            },
        ),
        migrations.CreateModel(
            name='FooterMenuBlock1Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Flatpage', verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b (\u0411\u043b\u043e\u043a 1)',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b (\u0411\u043b\u043e\u043a 1)',
            },
        ),
        migrations.CreateModel(
            name='FooterMenuBlock2Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Flatpage', verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041a\u0440\u0435\u0434\u0438\u0442 (\u0411\u043b\u043e\u043a 2)',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041a\u0440\u0435\u0434\u0438\u0442 (\u0411\u043b\u043e\u043a 2)',
            },
        ),
        migrations.CreateModel(
            name='FooterMenuBlock2Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Flatpage', verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 \u0434\u043b\u044f - \u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b (\u0411\u043b\u043e\u043a 2)',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b (\u0411\u043b\u043e\u043a 2)',
            },
        ),
        migrations.CreateModel(
            name='FooterMenuBlock3Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Flatpage', verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041a\u0440\u0435\u0434\u0438\u0442 (\u0411\u043b\u043e\u043a 3)',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041a\u0440\u0435\u0434\u0438\u0442 (\u0411\u043b\u043e\u043a 3)',
            },
        ),
        migrations.CreateModel(
            name='FooterMenuBlock3Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Flatpage', verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b (\u0411\u043b\u043e\u043a 3)',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e \u043f\u043e\u0434\u0432\u0430\u043b\u0430 - \u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b (\u0411\u043b\u043e\u043a 3)',
            },
        ),
    ]