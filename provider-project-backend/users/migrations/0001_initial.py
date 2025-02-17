# Generated by Django 2.2.5 on 2020-01-17 13:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, related_name='comapny_bind', to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('code', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descripiton', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, related_name='enterprise_team', to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descripiton', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, related_name='enterprise_sector', to='company.Company')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matriculation', models.BigIntegerField(blank=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('cpf', models.BigIntegerField(blank=True, null=True)),
                ('rg', models.IntegerField(blank=True, null=True)),
                ('genre', models.CharField(default='F', max_length=1)),
                ('recommendation', models.BooleanField(blank=True, default=False, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('complement', models.CharField(blank=True, max_length=150, null=True)),
                ('reference', models.CharField(blank=True, max_length=150, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('civil_sate', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('cell', models.CharField(blank=True, max_length=40, null=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/perfil')),
                ('anexo', models.FileField(blank=True, null=True, upload_to='anexo/doc/individual')),
                ('about', models.CharField(blank=True, max_length=150, null=True)),
                ('is_term_accepted', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('bind', models.ForeignKey(blank=True, null=True, on_delete=None, related_name='bind_user', to='users.Bind')),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=150)),
                ('discount', models.FloatField(max_length=200)),
                ('minimum_order', models.IntegerField()),
                ('value', models.FloatField(max_length=200)),
                ('amount_of_points', models.IntegerField()),
                ('value_of_points', models.FloatField(max_length=200)),
                ('start_point_range', models.IntegerField()),
                ('end_point_range', models.IntegerField()),
                ('term_payment', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, related_name='enterprise_level', to='company.Company')),
                ('type', models.ForeignKey(on_delete=None, to='users.Type')),
                ('user', models.ForeignKey(on_delete=None, related_name='person_level', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=150)),
                ('discount', models.FloatField(max_length=200)),
                ('minimum_order', models.IntegerField()),
                ('value', models.FloatField(max_length=200)),
                ('amount_of_points', models.IntegerField()),
                ('value_of_points', models.FloatField(max_length=200)),
                ('start_point_range', models.IntegerField()),
                ('end_point_range', models.IntegerField()),
                ('term_payment', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=None, related_name='enterprise_goal', to='company.Company')),
                ('type', models.ForeignKey(on_delete=None, to='users.Type')),
                ('user', models.ForeignKey(on_delete=None, related_name='person_goal', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('cell', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('main', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('company', models.ForeignKey(on_delete=None, related_name='enterprise_contact', to='company.Company')),
                ('user', models.ForeignKey(on_delete=None, related_name='person_contact', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='bind',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='users.Sector'),
        ),
        migrations.AddField(
            model_name='bind',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='users.Team'),
        ),
        migrations.AddField(
            model_name='bind',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='users.Type'),
        ),
        migrations.AddField(
            model_name='bind',
            name='user',
            field=models.ForeignKey(on_delete=None, related_name='user_bind', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bind',
            name='user_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='user_link', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField(blank=True, default=0, null=True)),
                ('agency', models.IntegerField(blank=True, default=0, null=True)),
                ('bank', models.CharField(blank=True, max_length=150, null=True)),
                ('type_account', models.CharField(blank=True, max_length=2, null=True)),
                ('kind_of_person', models.CharField(blank=True, max_length=2, null=True)),
                ('main', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('company', models.ForeignKey(on_delete=None, related_name='enterprise_bankAccount', to='company.Company')),
                ('user', models.ForeignKey(on_delete=None, related_name='person_bankAccount', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
