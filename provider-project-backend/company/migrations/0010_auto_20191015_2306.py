# Generated by Django 2.2.5 on 2019-10-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20191015_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='secret_key',
            field=models.CharField(blank=True, default='c50e76b080a7779c77c03609a738555ea0a022e33c3ec4cbb11e26bc8e4e91ffa059de5b07d38688ed03c42929d7184dcce2', max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='simples_key',
            field=models.CharField(blank=True, default='3f20139467d6782b6aea826bb5db99820767b1b8', max_length=125, null=True),
        ),
    ]
