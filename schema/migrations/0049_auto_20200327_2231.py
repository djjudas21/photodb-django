# Generated by Django 2.2 on 2020-03-27 22:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0048_auto_20200324_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameramodel',
            name='aperture_blades',
            field=models.PositiveIntegerField(
                blank=True, help_text='Number of aperture blades', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='closest_focus',
            field=models.PositiveIntegerField(
                blank=True, help_text='The closest focus possible with this lens, in cm', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='coating',
            field=models.CharField(blank=True, choices=[('Uncoated', 'Uncoated'), ('Single coated', 'Single coated'), (
                'Multi coated', 'Multi coated')], help_text='Type of lens coating', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='elements',
            field=models.PositiveIntegerField(
                blank=True, help_text='Number of optical lens elements', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='exif_lenstype',
            field=models.CharField(
                blank=True, help_text='EXIF LensID number, if this lens has one officially registered. See documentation at http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='filter_thread',
            field=models.DecimalField(
                blank=True, decimal_places=1, help_text='Diameter of lens filter thread, in mm', max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='formula',
            field=models.CharField(
                blank=True, help_text='Name of the type of lens formula (e.g. Tessar)', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='groups',
            field=models.PositiveIntegerField(
                blank=True, help_text='Number of optical groups', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='hood',
            field=models.CharField(
                blank=True, help_text='Model number of the compatible lens hood', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='image_circle',
            field=models.PositiveIntegerField(
                blank=True, help_text='Diameter of image circle projected by lens, in mm', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='lens_manufacturer',
            field=models.ForeignKey(blank=True, help_text='Manufacturer of this lens model', null=True,
                                    on_delete=django.db.models.deletion.CASCADE, related_name='lens_manufacturer', to='schema.Manufacturer'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='lens_model',
            field=models.CharField(
                blank=True, help_text='Model name of this lens', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='magnification',
            field=models.DecimalField(
                blank=True, decimal_places=3, help_text='Maximum magnification ratio of the lens, expressed like 0.765', max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='max_aperture',
            field=models.DecimalField(
                blank=True, decimal_places=1, help_text='Maximum (widest) aperture available on this lens (numerical part only, e.g. 2.8)', max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='max_focal_length',
            field=models.PositiveIntegerField(
                blank=True, help_text='Longest focal length of this lens, in mm', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='min_aperture',
            field=models.DecimalField(
                blank=True, decimal_places=1, help_text='Minimum (narrowest) aperture available on this lens (numerical part only, e.g. 22)', max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='min_focal_length',
            field=models.PositiveIntegerField(
                blank=True, help_text='Shortest focal length of this lens, in mm', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='nominal_max_angle_diag',
            field=models.PositiveIntegerField(blank=True, help_text='Nominal maximum diagonal field of view from manufacturer specs', null=True, validators=[
                                              django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)], verbose_name='Max angle of view'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='nominal_min_angle_diag',
            field=models.PositiveIntegerField(blank=True, help_text='Nominal minimum diagonal field of view from manufacturer specs', null=True, validators=[
                                              django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)], verbose_name='Min angle of view'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='rectilinear',
            field=models.BooleanField(
                blank=True, default=1, help_text='Whether this is a rectilinear lens', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='zoom',
            field=models.BooleanField(
                blank=True, help_text='Whether this is a zoom lens', null=True),
        ),
    ]
