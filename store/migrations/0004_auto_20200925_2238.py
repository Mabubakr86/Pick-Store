# Generated by Django 3.1.1 on 2020-09-25 20:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200925_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 20, 38, 11, 605699, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 20, 38, 11, 606697, tzinfo=utc)),
        ),
    ]
