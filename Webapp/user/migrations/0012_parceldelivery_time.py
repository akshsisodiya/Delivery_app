# Generated by Django 3.1.1 on 2020-12-28 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_parceldelivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceldelivery',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 28, 9, 34, 30, 577666, tzinfo=utc)),
        ),
    ]