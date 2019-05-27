# Generated by Django 2.0.6 on 2018-08-02 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0008_auto_20180715_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
