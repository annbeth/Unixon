# Generated by Django 2.0.6 on 2018-07-25 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_auto_20180725_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='orders.OrderDetails'),
        ),
    ]
