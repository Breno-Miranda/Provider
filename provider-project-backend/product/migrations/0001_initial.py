# Generated by Django 2.2.5 on 2020-01-17 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('taxation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('initials', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=False)),
                ('discount', models.FloatField(max_length=200)),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('initials', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, related_name='status_product', to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.BigIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('ean', models.BigIntegerField(blank=True, default=False, null=True)),
                ('ncm', models.CharField(blank=True, max_length=150, null=True)),
                ('unidade', models.CharField(blank=True, max_length=150, null=True)),
                ('cest', models.BigIntegerField(blank=True, default=False, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('origin', models.IntegerField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, max_length=200, null=True)),
                ('resale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('page', models.BigIntegerField(blank=True, null=True)),
                ('value_provider', models.DecimalField(blank=True, decimal_places=2, max_digits=10, max_length=255, null=True)),
                ('type_value_provider', models.CharField(blank=True, max_length=255, null=True)),
                ('stock', models.BigIntegerField(default=0)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('last_date', models.DateTimeField(blank=True, null=True)),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Catalog')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=None, to='product.Category')),
                ('company', models.ForeignKey(blank=True, on_delete=None, to='company.Company')),
                ('status', models.ForeignKey(blank=True, on_delete=None, to='product.Status')),
                ('taxation', models.ForeignKey(blank=True, on_delete=None, to='taxation.Tax')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='products')),
                ('url_thubnail', models.CharField(blank=True, max_length=150, null=True)),
                ('initials', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
                ('product', models.ForeignKey(on_delete=None, to='product.Product')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('initials', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
