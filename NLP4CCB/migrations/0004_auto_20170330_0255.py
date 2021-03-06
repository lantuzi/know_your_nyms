# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-30 02:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NLP4CCB', '0003_auto_20170323_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=140)),
                ('is_pending', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='relation',
            name='model_score',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='word_net_score',
        ),
        migrations.RemoveField(
            model_name='userinput',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='userinput',
            name='round_time',
        ),
        migrations.AddField(
            model_name='relation',
            name='challenge_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relation',
            name='in_word_net',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userstat',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userstat',
            name='rounds_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userstat',
            name='total_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='challenge',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NLP4CCB.Relation'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
