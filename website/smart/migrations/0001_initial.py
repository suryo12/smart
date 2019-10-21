# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-10 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tegangan', models.CharField(max_length=1000)),
                ('arus', models.FloatField(blank=True, default=None, null=True)),
                ('daya', models.CharField(max_length=1000)),
                ('tanggal', models.DateField(db_index=True, default=None, null=True)),
                ('waktu', models.TimeField(db_index=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NodeID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=250)),
                ('alamat', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='node_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.NodeID'),
        ),
    ]