# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pet_health', models.IntegerField(default=100)),
                ('virtual_gold', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Saving_Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('budget', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='saving_account',
            name='username',
            field=models.ForeignKey(to='egg.User'),
        ),
        migrations.AddField(
            model_name='pet',
            name='username',
            field=models.ForeignKey(to='egg.User'),
        ),
    ]
