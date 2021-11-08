# Generated by Django 2.2.23 on 2021-07-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0127_auto_20210716_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.CharField(blank=True, choices=[('Individual', 'Individual'), ('Business', 'Business')], help_text='Type of person or business', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text='Name of the person or business', max_length=45, unique=True),
        ),
    ]