# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Comment(models.Model):
    parkid = models.CharField(db_column='parkId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parkname = models.CharField(db_column='parkName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    commenttext = models.CharField(db_column='commentText', max_length=100, blank=True, null=True)  # Field name made lowercase.
    star = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'

class Parkinginfo(models.Model):
    id = models.IntegerField(primary_key=True)
    areaid = models.IntegerField(db_column='areaId', blank=True, null=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='areaName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkname = models.CharField(db_column='parkName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalspace = models.IntegerField(db_column='totalSpace', blank=True, null=True)  # Field name made lowercase.
    surplusspace = models.CharField(db_column='surplusSpace', max_length=10, blank=True, null=True)  # Field name made lowercase.
    payguide = models.CharField(db_column='payGuide', max_length=255, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    parkid = models.CharField(db_column='parkId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    update_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parkinginfo'


class User(models.Model):
    user = models.CharField(max_length=50, blank=True, null=True)
    nick = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    createdt = models.DateTimeField(db_column='createDt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
