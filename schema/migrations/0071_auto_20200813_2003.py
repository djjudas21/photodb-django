# Generated by Django 2.2.14 on 2020-08-13 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0070_metering'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='negativesize',
            options={'ordering': ['name'], 'verbose_name_plural': 'negative sizes'},
        ),
    ]
