# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-17 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recent_events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('heading', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='eventimages/pictures')),
                ('content', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]