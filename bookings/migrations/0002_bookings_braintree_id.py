# Generated by Django 2.2.2 on 2020-08-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
