# Generated by Django 3.1.1 on 2020-09-25 20:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200925_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 20, 14, 4, 104130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 20, 14, 4, 105132, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
