# Generated by Django 2.2.5 on 2019-10-26 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0025_auto_20191026_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='secret_key',
            field=models.CharField(blank=True, default=b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55IjoxfQ.2wxqwX2wLSsXX7pj50VWBWkTM8e294eREKh_G_AT4Ws', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='simples_key',
            field=models.CharField(blank=True, default=b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55IjoxfQ.2wxqwX2wLSsXX7pj50VWBWkTM8e294eREKh_G_AT4Ws', max_length=255, null=True),
        ),
    ]
