# Generated by Django 2.2.2 on 2020-04-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0018_auto_20200401_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avg_rating',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_rates',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
