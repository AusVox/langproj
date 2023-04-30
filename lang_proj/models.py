# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Courses(models.Model):
    id = models.AutoField(primary_key=True, db_column='course_id')
    name = models.CharField(blank=True, null=True, max_length=100)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Courses'


class Terms(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    course_id = models.IntegerField(db_column='course_id')
    word = models.CharField(blank=True, null=True, max_length=100)
    translation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Terms'
