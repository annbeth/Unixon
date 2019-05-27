# Generated by Django 2.0.6 on 2018-07-26 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0040_auto_20180725_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='phone_number',
            field=models.CharField(max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='phone number must be entered in the format +254... up to 12 digits allowed', regex='^\\+?1?\\d{2,12}$')]),
        ),
    ]
