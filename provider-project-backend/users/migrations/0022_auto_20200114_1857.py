# Generated by Django 2.2.5 on 2020-01-14 18:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0021_auto_20200114_0207'),
    ]

    operations = [
       migrations.AlterField(
            model_name='profile',
            name='rg',
            field=models.IntegerField(blank=True, null=True),
        )

    ]
