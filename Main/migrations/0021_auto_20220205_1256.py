# Generated by Django 3.1.1 on 2022-02-05 07:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0020_notification_notification_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 7, 26, 24, 59699, tzinfo=utc)),
        ),
    ]