# Generated by Django 2.2.4 on 2019-09-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0035_auto_20190920_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toning',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='accessory',
            name='camera_model_compatibility',
            field=models.ManyToManyField(blank=True, to='schema.CameraModel'),
        ),
    ]