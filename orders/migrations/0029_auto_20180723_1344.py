# Generated by Django 2.0.6 on 2018-07-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_auto_20180723_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
