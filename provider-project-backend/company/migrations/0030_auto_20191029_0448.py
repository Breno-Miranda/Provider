# Generated by Django 2.2.5 on 2019-10-29 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0029_auto_20191028_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='secret_key',
            field=models.CharField(blank=True, default=b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55IjoiZTgxYjRjMTFhZTk1ODA5MjEzN2YzYzUyZTM2N2IzYWVhY2M5OWEyOTIwMDVhMjRkNjMzYTI5NWM1NWM4YzM1YWZjMzgzNjg5MzUwZDJlMmQ0MDE2ZmU3ZDExZDE1N2IyZjczMCJ9.D-qUCtyJ1Ju7soV_mrS1sKG7Bgr3iBEKnsuakcXt6ps', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='simples_key',
            field=models.CharField(blank=True, default=b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55IjoiMTdhMTFmYjliMDRlNTJjYjBlYjdlODE3MmZlYzhiNmRjM2YyOTlkOCJ9.7zYdO5W540NfMZnvP63IelllZrQApLG7O4cJmazrB-w', max_length=255, null=True),
        ),
    ]
