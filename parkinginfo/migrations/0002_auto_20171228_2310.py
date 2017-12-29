# Generated by Django 2.0 on 2017-12-28 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkinginfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkid', models.CharField(blank=True, db_column='parkId', max_length=50, null=True)),
                ('parkname', models.CharField(blank=True, db_column='parkName', max_length=50, null=True)),
                ('commenttext', models.CharField(blank=True, db_column='commentText', max_length=100, null=True)),
                ('star', models.IntegerField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('nick', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('createdt', models.DateTimeField(blank=True, db_column='createDt', null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='parkinginfo',
            options={'managed': False},
        ),
    ]