# Generated by Django 2.1.10 on 2019-08-13 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0005_auto_20190813_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquired', models.DateField(verbose_name='Date on which the camera was acquired')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price paid for this camera')),
                ('serial', models.CharField(max_length=45, verbose_name='Serial number of the camera')),
                ('datecode', models.CharField(max_length=45, verbose_name='Date code of the camera, if different from the serial number')),
                ('manufactured', models.IntegerField(verbose_name='Year of manufacture of the camera')),
                ('own', models.BooleanField(verbose_name='Whether the camera is currently owned')),
                ('notes', models.CharField(max_length=100, verbose_name='Freeform text field for extra notes')),
                ('lost', models.DateField(verbose_name='Date on which the camera was lost/sold/etc')),
                ('lost_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price at which the camera was sold')),
                ('source', models.CharField(max_length=150, verbose_name='Where the camera was acquired from')),
                ('condition_notes', models.CharField(max_length=150, verbose_name='Description of condition')),
            ],
        ),
        migrations.CreateModel(
            name='CameraModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='The model name of the camera')),
                ('metering', models.BooleanField(verbose_name='Whether the camera has built-in metering')),
                ('coupled_metering', models.BooleanField(verbose_name='Whether the cameras meter is coupled automatically')),
                ('weight', models.IntegerField(verbose_name='Weight of the camera body (without lens or batteries) in grammes (g)')),
                ('introduced', models.IntegerField(verbose_name='Year in which the camera model was introduced')),
                ('discontinued', models.IntegerField(verbose_name='Year in which the camera model was discontinued')),
                ('shutter_model', models.CharField(max_length=45, verbose_name='Model of shutter')),
                ('cable_release', models.BooleanField(verbose_name='Whether the camera has the facility for a remote cable release')),
                ('viewfinder_coverage', models.IntegerField(verbose_name='Percentage coverage of the viewfinder. Mostly applicable to SLRs.')),
                ('power_drive', models.BooleanField(verbose_name='Whether the camera has models.IntegerFieldegrated motor drive')),
                ('continuous_fps', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='The maximum rate at which the camera can shoot, in frames per second')),
                ('video', models.BooleanField(verbose_name='Whether the camera can take video/movie')),
                ('digital', models.BooleanField(verbose_name='Whether this is a digital camera')),
                ('fixed_mount', models.BooleanField(verbose_name='Whether the camera has a fixed lens')),
                ('battery_qty', models.IntegerField(verbose_name='Quantity of batteries needed')),
                ('notes', models.CharField(max_length=100, verbose_name='Freeform text field for extra notes')),
                ('bulb', models.BooleanField(verbose_name='Whether the camera supports bulb (B) exposure')),
                ('time', models.BooleanField(verbose_name='Whether the camera supports time (T) exposure')),
                ('min_iso', models.IntegerField(verbose_name='Minimum ISO the camera will accept for metering')),
                ('max_iso', models.IntegerField(verbose_name='Maximum ISO the camera will accept for metering')),
                ('af_points', models.IntegerField(verbose_name='Number of autofocus points')),
                ('int_flash', models.BooleanField(verbose_name='Whether the camera has an integrated flash')),
                ('int_flash_gn', models.IntegerField(verbose_name='Guide number of internal flash')),
                ('ext_flash', models.BooleanField(verbose_name=' Whether the camera supports an external flash')),
                ('pc_sync', models.BooleanField(verbose_name='Whether the camera has a PC sync socket for flash')),
                ('hotshoe', models.BooleanField(verbose_name='Whether the camera has a hotshoe')),
                ('coldshoe', models.BooleanField(verbose_name='Whether the camera has a coldshoe or accessory shoe')),
                ('meter_min_ev', models.IntegerField(verbose_name='Lowest EV/LV the built-in meter supports')),
                ('meter_max_ev', models.IntegerField(verbose_name='Highest EV/LV the built-in meter supports')),
                ('dof_preview', models.BooleanField(verbose_name='Whether the camera has depth of field preview')),
                ('tripod', models.BooleanField(verbose_name='Whether the camera has a tripod bush')),
                ('battery_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Battery')),
                ('body_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.BodyType')),
                ('flash_metering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.FlashProtocol')),
                ('focus_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.FocusType')),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Format')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Name of the developer')),
                ('for_paper', models.BooleanField(verbose_name='Whether this developer can be used with paper')),
                ('for_film', models.BooleanField(verbose_name='Whether this developer can be used with film')),
                ('chemistry', models.CharField(max_length=45, verbose_name='The key chemistry on which this developer is based (e.g. phenidone)')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Enlarger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Name/model of the enlarger')),
                ('acquired', models.DateField(verbose_name='Date on which the enlarger was acquired')),
                ('lost', models.DateField(verbose_name='Date on which the enlarger was lost/sold')),
                ('introduced', models.IntegerField(verbose_name='Year in which the enlarger was introduced')),
                ('discontinued', models.IntegerField(verbose_name='Year in which the enlarger was discontinued')),
                ('cost', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='Purchase cost of the enlarger')),
                ('lost_price', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='Sale price of the enlarger')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Manufacturer')),
                ('negative_size_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.NegativeSize')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exposed_at', models.IntegerField(verbose_name='ISO at which the film was exposed')),
                ('date_loaded', models.DateField(verbose_name='Date when the film was loaded into a camera')),
                ('date_processed', models.DateField(verbose_name='Date when the film was processed')),
                ('title', models.CharField(max_length=150, verbose_name='Title of the film')),
                ('frames', models.IntegerField(verbose_name='Expected (not actual) number of frames from the film')),
                ('directory', models.CharField(max_length=100, verbose_name='Name of the directory that contains the scanned images from this film')),
                ('dev_uses', models.IntegerField(verbose_name='Number of previous uses of the developer')),
                ('dev_time', models.DurationField(verbose_name='Duration of development')),
                ('dev_temp', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Temperature of development')),
                ('dev_n', models.IntegerField(verbose_name='Number of the Push/Pull rating of the film, e.g. N+1, N-2')),
                ('development_notes', models.CharField(max_length=200, verbose_name='Extra freeform notes about the development process')),
                ('bulk_film_loaded', models.DateField(verbose_name='Date that this film was cut from a bulk roll')),
                ('film_batch', models.CharField(max_length=45, verbose_name='Batch number of the film')),
                ('expiry_date', models.DateField(verbose_name='Expiry date of the film')),
                ('purchase_date', models.DateField(verbose_name='Date this film was purchased')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price paid for this film')),
                ('processed_by', models.CharField(max_length=45, verbose_name='Person or place that processed this film')),
                ('archive_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Archive')),
                ('bulk_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.BulkFilm')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Camera')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Developer')),
                ('filmstock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.FilmStock')),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Format')),
            ],
        ),
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=45, verbose_name='Serial number of this lens')),
                ('date_code', models.CharField(max_length=45, verbose_name='Date code of this lens, if different from the serial number')),
                ('manufactured', models.IntegerField(verbose_name='Year in which this specific lens was manufactured')),
                ('acquired', models.DateField(verbose_name='Date on which this lens was acquired')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price paid for this lens')),
                ('notes', models.CharField(max_length=45, verbose_name='Freeform notes field')),
                ('own', models.BooleanField(verbose_name='Whether we currently own this lens')),
                ('lost', models.DateField(verbose_name='Date on which lens was lost/sold/disposed')),
                ('lost_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price for which the lens was sold')),
                ('source', models.CharField(max_length=150, verbose_name='Place where the lens was acquired from')),
                ('condition_notes', models.CharField(max_length=150, verbose_name='Description of condition')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Condition')),
            ],
        ),
        migrations.CreateModel(
            name='LensModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45, verbose_name='Model name of this lens')),
                ('zoom', models.BooleanField(verbose_name='Whether this is a zoom lens')),
                ('min_focal_length', models.IntegerField(verbose_name='Shortest focal length of this lens, in mm')),
                ('max_focal_length', models.IntegerField(verbose_name='Longest focal length of this lens, in mm')),
                ('closest_focus', models.IntegerField(verbose_name='The closest focus possible with this lens, in cm')),
                ('max_aperture', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Maximum (widest) aperture available on this lens (numerical part only, e.g. 2.8)')),
                ('min_aperture', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Minimum (narrowest) aperture available on this lens (numerical part only, e.g. 22)')),
                ('elements', models.IntegerField(verbose_name='Number of optical lens elements')),
                ('groups', models.IntegerField(verbose_name='Number of optical groups')),
                ('weight', models.IntegerField(verbose_name='Weight of this lens, in grammes (g)')),
                ('nominal_min_angle_diag', models.IntegerField(verbose_name='Nominal minimum diagonal field of view from manufacturer specs')),
                ('nominal_max_angle_diag', models.IntegerField(verbose_name='Nominal maximum diagonal field of view from manufacturer specs')),
                ('aperture_blades', models.IntegerField(verbose_name='Number of aperture blades')),
                ('autofocus', models.BooleanField(verbose_name='Whether this lens has autofocus capability')),
                ('filter_thread', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Diameter of lens filter thread, in mm')),
                ('magnification', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Maximum magnification ratio of the lens, expressed like 0.765')),
                ('url', models.URLField(verbose_name='URL to more information about this lens')),
                ('introduced', models.IntegerField(verbose_name='Year in which this lens model was introduced')),
                ('discontinued', models.IntegerField(verbose_name='Year in which this lens model was discontinued')),
                ('fixed_mount', models.BooleanField(verbose_name='Whether this is a fixed lens (i.e. on a compact camera)')),
                ('notes', models.CharField(max_length=100, verbose_name='Freeform notes field')),
                ('coating', models.CharField(max_length=45, verbose_name='Notes about the lens coating type')),
                ('hood', models.CharField(max_length=45, verbose_name='Model number of the compatible lens hood')),
                ('exif_lenstype', models.CharField(max_length=45, verbose_name='EXIF LensID number, if this lens has one officially registered. See documentation at http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/')),
                ('rectilinear', models.BooleanField(verbose_name='Whether this is a rectilinear lens')),
                ('length', models.IntegerField(verbose_name='Length of lens in mm')),
                ('diameter', models.IntegerField(verbose_name='Width of lens in mm')),
                ('image_circle', models.IntegerField(verbose_name='Diameter of image circle projected by lens, in mm')),
                ('formula', models.CharField(max_length=45, verbose_name='Name of the type of lens formula (e.g. Tessar)')),
                ('shutter_model', models.CharField(max_length=45, verbose_name='Name of the integrated shutter, if any')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Manufacturer')),
                ('mount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Mount')),
                ('negative_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.NegativeSize')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='Title of this movie')),
                ('description', models.CharField(max_length=200, verbose_name='Description of this movie')),
                ('sound', models.BooleanField(verbose_name='Whether this movie has sound')),
                ('fps', models.IntegerField(verbose_name='Frame rate of this movie, in fps')),
                ('feet', models.IntegerField(verbose_name='Length of this movie in feet')),
                ('duration', models.DurationField(verbose_name='Duration of this movie')),
                ('date_loaded', models.DateField(verbose_name='Date that the filmstock was loaded into a camera')),
                ('date_shot', models.DateField(verbose_name='Date on which this movie was shot')),
                ('date_processed', models.DateField(verbose_name='Date on which this movie was processed')),
                ('camera_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Camera')),
                ('filmstock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.FilmStock')),
                ('format_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Format')),
                ('lens_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Lens')),
                ('process_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Process')),
            ],
        ),
        migrations.CreateModel(
            name='Negative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.CharField(max_length=8, verbose_name='Frame number or code of this negative')),
                ('caption', models.CharField(max_length=150, verbose_name='Caption of this picture')),
                ('date', models.DateTimeField(verbose_name='Date & time on which this picture was taken')),
                ('aperture', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Aperture used to take this picture (numerical part only)')),
                ('notes', models.CharField(max_length=200, verbose_name='Extra freeform notes about this exposure')),
                ('focal_length', models.IntegerField(verbose_name='If a zoom lens was used, specify the focal length of the lens')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitude of the location where the picture was taken')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitude of the location where the picture was taken')),
                ('flash', models.BooleanField(verbose_name='Whether flash was used')),
                ('exposure_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.ExposureProgram')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Film')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Filter')),
                ('lens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Lens')),
                ('metering_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.MeteringMode')),
                ('photographer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Person')),
                ('shutter_speed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.ShutterSpeed')),
                ('teleconverter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Teleconverter')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField(verbose_name='Width of print to be made')),
                ('height', models.IntegerField(verbose_name='Height of print to be made')),
                ('added', models.DateField(verbose_name='Date that the order was placed')),
                ('printed', models.BooleanField(verbose_name='Whether the print has been made')),
                ('negative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Negative')),
            ],
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='The date that the print was made')),
                ('height', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Height of the print in inches')),
                ('width', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Width of the print in inches')),
                ('aperture', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Aperture used to make this print (numerical part only, e.g. 5.6)')),
                ('exposure_time', models.DurationField(verbose_name='Exposure time of this print')),
                ('filtration_grade', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Contrast grade of paper used')),
                ('development_time', models.DurationField(verbose_name='Development time of this print')),
                ('bleach_time', models.DurationField(verbose_name='Duration of bleaching')),
                ('toner_dilution', models.CharField(max_length=8, verbose_name='Dilution of the first toner used to make this print')),
                ('toner_time', models.DurationField(verbose_name='Duration of first toning')),
                ('own', models.BooleanField(verbose_name='Whether we currently own this print')),
                ('location', models.CharField(max_length=100, verbose_name='The place where this print is currently')),
                ('sold_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sale price of the print')),
                ('fine', models.BooleanField(verbose_name='Whether this is a fine print')),
                ('notes', models.CharField(max_length=200, verbose_name='Freeform notes about this print, e.g. dodging, burning & complex toning')),
                ('archive_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Archive')),
                ('developer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Developer')),
                ('enlarger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Enlarger')),
                ('lens_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Lens')),
                ('negative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Negative')),
                ('paper_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.PaperStock')),
                ('printer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Person')),
                ('toner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Toner')),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='The date of the repair')),
                ('summary', models.CharField(max_length=100, verbose_name='Brief summary of the repair')),
                ('description', models.CharField(max_length=500, verbose_name='Longer description of the repair')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Camera')),
                ('lens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Lens')),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128, verbose_name='Filename of the scan')),
                ('date', models.DateField(verbose_name='Date that this scan was made')),
                ('colour', models.BooleanField(verbose_name='Whether this is a colour image')),
                ('width', models.IntegerField(verbose_name='Width of the scanned image in pixels')),
                ('height', models.IntegerField(verbose_name='Height of the scanned image in pixels')),
                ('negative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Negative')),
                ('print_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Print')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='print_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Print'),
        ),
        migrations.AddField(
            model_name='order',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Person'),
        ),
        migrations.AddField(
            model_name='lens',
            name='lensmodel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.LensModel'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='lensmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.LensModel'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Manufacturer'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='metering_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.MeteringType'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='mount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Mount'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='negative_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.NegativeSize'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='shutter_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.ShutterType'),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='x_sync',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.ShutterSpeed'),
        ),
        migrations.AddField(
            model_name='camera',
            name='cameramodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.CameraModel'),
        ),
        migrations.AddField(
            model_name='camera',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Condition'),
        ),
        migrations.AddField(
            model_name='camera',
            name='lens',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Lens'),
        ),
    ]
