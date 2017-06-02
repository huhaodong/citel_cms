
'''
    this model well created some table for build a database
'''

# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''
    this table well restore some items data
'''

class items(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content_path = models.FilePathField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return  self.name

'''
    this table well restore the user account info
'''

class user_account(models.Model):
    user_name = models.CharField(max_length=200)
    user_md5 = models.CharField(max_length=300)
    user_email = models.EmailField(unique=True)
    user_phone = models.CharField(max_length=30)
    user_privilege_level = models.IntegerField()
    user_account_level = models.IntegerField()
    user_account_point = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return  self.user_name

'''
    this table well restore the admin account info
'''

class admin_account(models.Model):
    admin_name = models.CharField(max_length=200)
    admin_md5 = models.CharField(max_length=300)
    admin_email = models.EmailField(unique=True)
    admin_phone = models.CharField(max_length=30)
    admin_privilege_level = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return  self.admin_name