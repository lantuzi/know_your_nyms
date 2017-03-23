# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 02:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('base_word', models.CharField(max_length=50)),
                ('input_word', models.CharField(max_length=50)),
                ('word_net_score', models.FloatField()),
                ('model_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('round_time', models.IntegerField()),
                ('word_score', models.FloatField()),
                ('challenge', models.BooleanField()),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NLP4CCB.Relation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds_played', models.IntegerField()),
                ('total_score', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
