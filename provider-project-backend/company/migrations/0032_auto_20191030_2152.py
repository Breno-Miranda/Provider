# Generated by Django 2.2.5 on 2019-10-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0031_auto_20191029_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='secret_key',
            field=models.CharField(blank=True, default=b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55IjoiYzFjMTliYzY5MTA1NGZlYWJkMDRmNTcyZWFmZjUwMWRlMGI5NWNlOWQ5NWEyMTcxOGQ1Y2I2MDUyOGMwZmI0MDQ3ZjU5MzllZTFhODJlNzg0MGU3NTMxNDliNWI2ODk2YzYyNCJ9.KkGPcQ1x3T2MlYzbb6KVDPXbCoYpA9uxsFO4gf3qA6o', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='simples_key',
            field=models.CharField(blank=True, default=b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55IjoiMDVkNWJkNmE5ZmZiMGQ2MjFiYjZmODlhMDQ5OGM4YjdlYzE0ZmQ3ZSJ9.APpC6iR9YtEQJ-nxLnvse_uGBeNxEXTDVP2knsta-Pw', max_length=255, null=True),
        ),
    ]
