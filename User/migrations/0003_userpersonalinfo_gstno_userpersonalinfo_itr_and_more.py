# Generated by Django 4.1.3 on 2023-12-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_userpersonalinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersonalinfo',
            name='gstno',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='userpersonalinfo',
            name='itr',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='userpersonalinfo',
            name='turnover',
            field=models.CharField(default='', max_length=10),
        ),
    ]
