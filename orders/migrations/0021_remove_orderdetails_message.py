# Generated by Django 2.0.6 on 2018-07-16 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20180716_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='message',
        ),
    ]
