# Generated by Django 2.0.6 on 2018-07-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_order_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
