# Generated by Django 2.0.6 on 2018-07-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_order_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='message',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
