# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=200)),
                ('admin_md5', models.CharField(max_length=300)),
                ('admin_email', models.EmailField(max_length=254, unique=True)),
                ('admin_phone', models.CharField(max_length=30)),
                ('admin_privilege_level', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('content_path', models.FilePathField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_md5', models.CharField(max_length=300)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_phone', models.CharField(max_length=30)),
                ('user_privilege_level', models.IntegerField()),
                ('user_account_level', models.IntegerField()),
                ('user_account_point', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
