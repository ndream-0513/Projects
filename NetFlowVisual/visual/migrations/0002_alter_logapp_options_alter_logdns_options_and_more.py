# Generated by Django 4.2.10 on 2024-02-26 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logapp',
            options={'managed': False, 'verbose_name': '应用日志', 'verbose_name_plural': '应用日志'},
        ),
        migrations.AlterModelOptions(
            name='logdns',
            options={'managed': False, 'verbose_name': 'DNS日志', 'verbose_name_plural': 'DNS日志'},
        ),
        migrations.AlterModelOptions(
            name='lognetflow',
            options={'managed': False, 'verbose_name': 'TCP/UDP日志', 'verbose_name_plural': 'TCP/UDP日志'},
        ),
    ]
