# Generated by Django 2.2.5 on 2020-01-11 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.BigIntegerField()),
                ('company_name', models.CharField(max_length=150)),
                ('social_name', models.CharField(max_length=150)),
                ('fancy_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('complement', models.CharField(max_length=150)),
                ('reference', models.CharField(max_length=150)),
                ('neighborhood', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField()),
                ('number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=150)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('is_term_accepted', models.BooleanField(default=False)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('initials', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=150)),
                ('provider', models.ForeignKey(on_delete=None, to='common.Provider')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('commission', models.FloatField(blank=True, null=True)),
                ('initials', models.CharField(max_length=3)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='catalog')),
                ('pdf', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_date', models.DateTimeField(blank=True, null=True)),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Zone')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
