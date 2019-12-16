# Generated by Django 2.2.5 on 2019-09-13 19:32

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
        ('request', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accrediting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cnpj', models.BigIntegerField()),
                ('number_code', models.CharField(blank=True, max_length=50, null=True)),
                ('initials', models.CharField(blank=True, max_length=1, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Flags_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
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
        migrations.CreateModel(
            name='Nature_operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Payment_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
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
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('initials', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, related_name='status_sale', to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finality', models.IntegerField(choices=[(1, 'NF-e normal'), (4, 'Devolução/Retorno')], default=1)),
                ('operation', models.IntegerField(choices=[(1, 'Saída'), (0, 'Entrada')], default=1)),
                ('template', models.IntegerField(choices=[(1, 'NF-e'), (2, 'NFC-e')], default=2)),
                ('ambiente', models.IntegerField(choices=[(1, '1 - Produção'), (2, '2 - Homologação')], default=2)),
                ('payment_form_amount', models.IntegerField(blank=True, null=True)),
                ('integration_type', models.IntegerField(choices=[(1, '1 - Pagamento integrado com o sistema de automação da empresa (Ex: equipamento TEF, Comércio eletrônico)'), (2, '2 - Pagamento não integrado com o sistema de automação da empresa (Ex: equipamento POS)')], default=2)),
                ('nsu_authorization', models.BigIntegerField(blank=True, default=False, null=True)),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('presence', models.IntegerField(choices=[(0, '0 - Não se aplica (por exemplo, Nota Fiscal complementar ou de ajuste)'), (1, '1 - Operação presencial'), (2, '2 - Operação não presencial, pela Internet'), (3, '3 - Operação não presencial, Teleatendimento'), (4, '4 - NFC-e em operação com entrega a domicílio'), (5, '5 - Operação presencial, fora do estabelecimento'), (9, '9 - Operação não presencial, outros')], default=1)),
                ('free_model', models.IntegerField(choices=[(0, '0 - Contratação do Frete por conta do Remetente (CIF)'), (2, '1 - Contratação do Frete por conta do Destinatário (FOB)'), (1, '2 - Contratação do Frete por conta de Terceiros'), (2, '3 - Transporte Próprio por conta do Remetente'), (4, '4 - Transporte Próprio por conta do Destinatário'), (9, '9 - Sem Ocorrência de Transporte')], default=3)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('freight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_register', models.DateTimeField(auto_now=True)),
                ('accrediting', models.ForeignKey(blank=True, null=True, on_delete=None, to='sale.Accrediting')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=None, to='users.Busines')),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
                ('flags_card', models.ForeignKey(blank=True, null=True, on_delete=None, to='sale.Flags_card')),
                ('individual', models.ForeignKey(blank=True, null=True, on_delete=None, to='users.Individual')),
                ('nature_operation', models.ForeignKey(blank=True, null=True, on_delete=None, to='sale.Nature_operation')),
                ('payment_form', models.ForeignKey(blank=True, null=True, on_delete=None, to='sale.Payment_form')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=None, to='request.Request')),
                ('status', models.ForeignKey(blank=True, default=1, null=True, on_delete=None, to='sale.Status')),
                ('user', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
