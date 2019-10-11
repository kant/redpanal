# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-08 00:35
from __future__ import unicode_literals

from django.db import migrations
from users.models import DEFAULT_GROUP

def create_default_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    User = apps.get_model('auth', 'User')
    Permission = apps.get_model('auth', 'Permission')

    default_group, created = Group.objects.get_or_create(name=DEFAULT_GROUP)
    if created:
        add_audio = Permission.objects.get(codename='add_audio')
        default_group.permissions.add(add_audio)
        default_group.save()

    users = apps.get_model('auth', 'User')
    for user in User.objects.all():
        user.groups.add(default_group)
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
    ]

    operations = [
         migrations.RunPython(create_default_group),
    ]
