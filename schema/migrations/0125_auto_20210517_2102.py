# Generated by Django 2.2.20 on 2021-05-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0124_auto_20210428_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameramodel',
            name='focus_type',
            field=models.CharField(blank=True, choices=[('Autofocus', 'Autofocus'), ('Fixed focus', 'Fixed focus'), ('Zone_focus', 'Manual focus (zone focus)'), ('Rangefinder', 'Manual focus (rangefinder)'), ('SLR', 'Manual focus (SLR)'), ('TLR', 'Manual focus (TLR)'), ('View_camera', 'Manual focus (view camera)')], help_text='Focus type used on this camera model', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcameramodel',
            name='focus_type',
            field=models.CharField(blank=True, choices=[('Autofocus', 'Autofocus'), ('Fixed focus', 'Fixed focus'), ('Zone_focus', 'Manual focus (zone focus)'), ('Rangefinder', 'Manual focus (rangefinder)'), ('SLR', 'Manual focus (SLR)'), ('TLR', 'Manual focus (TLR)'), ('View_camera', 'Manual focus (view camera)')], help_text='Focus type used on this camera model', max_length=25, null=True),
        ),
    ]