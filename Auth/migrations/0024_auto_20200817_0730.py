# Generated by Django 2.2.2 on 2020-08-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0023_auto_20200817_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]