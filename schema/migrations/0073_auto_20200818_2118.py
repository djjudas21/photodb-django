# Generated by Django 2.2.14 on 2020-08-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0072_auto_20200816_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalnegativesize',
            name='diagonal',
            field=models.DecimalField(blank=True, decimal_places=1, editable=False, help_text='Diagonal of the negative size in mm', max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='negativesize',
            name='diagonal',
            field=models.DecimalField(blank=True, decimal_places=1, editable=False, help_text='Diagonal of the negative size in mm', max_digits=5, null=True),
        ),
    ]
