# Generated by Django 2.2.5 on 2019-10-15 23:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20191015_2306'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_auto_20191015_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='busines',
            name='anexo',
            field=models.ImageField(default='settings.MEDIA_ROOT', upload_to='anexo/doc/business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busines',
            name='recommendation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='anexo',
            field=models.ImageField(default='settings.MEDIA_ROOT', upload_to='anexo/doc/collaborator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collaborator',
            name='genre',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collaborator',
            name='recommendation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='cell',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='anexo',
            field=models.ImageField(default='settings.MEDIA_ROOT', upload_to='anexo/doc/individual'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='genre',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='name_complete',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='recommendation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField(blank=True, default=0, null=True)),
                ('agency', models.IntegerField(blank=True, default=0, null=True)),
                ('bank', models.CharField(blank=True, max_length=150, null=True)),
                ('type_account', models.CharField(blank=True, max_length=150, null=True)),
                ('kind_of_person', models.CharField(blank=True, max_length=150, null=True)),
                ('company', models.ForeignKey(on_delete=None, related_name='enterprise_bankAccount', to='company.Company')),
                ('user', models.ForeignKey(on_delete=None, related_name='person_bankAccount', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
