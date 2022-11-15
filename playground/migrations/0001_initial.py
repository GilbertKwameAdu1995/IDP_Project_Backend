# Generated by Django 4.1.2 on 2022-11-15 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_feature', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HyperSpectralImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hyperspec_image', models.CharField(max_length=200)),
                ('imaging_data', models.CharField(max_length=200)),
                ('resolution', models.CharField(max_length=200)),
                ('bands', models.CharField(max_length=200)),
                ('frames', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MultimodalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preop_mri', models.CharField(max_length=200)),
                ('postop_mri', models.CharField(max_length=200)),
                ('biopsy', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RgbImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anatomical_annot', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TissueClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tissue_type', models.CharField(max_length=200)),
                ('class_feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.classfeature')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('hyper_spectral_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.hyperspectralimage')),
                ('multi_modal_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.multimodaldata')),
            ],
        ),
        migrations.CreateModel(
            name='Mask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mask_image', models.CharField(max_length=200)),
                ('diagnosis', models.ManyToManyField(to='playground.diagnosis')),
                ('tissue_class', models.ManyToManyField(to='playground.tissueclass')),
            ],
        ),
        migrations.CreateModel(
            name='Imaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquisition_type', models.CharField(max_length=200)),
                ('light_intensity', models.CharField(max_length=200)),
                ('light_source', models.CharField(max_length=200)),
                ('device_name', models.CharField(max_length=200)),
                ('hyper_spectral_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.hyperspectralimage')),
            ],
        ),
        migrations.AddField(
            model_name='hyperspectralimage',
            name='rgb_image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='playground.rgbimage'),
        ),
        migrations.CreateModel(
            name='HsiSoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_method', models.CharField(max_length=200)),
                ('analysis_duration', models.CharField(max_length=200)),
                ('imaging', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.imaging')),
            ],
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annot_image', models.CharField(max_length=200)),
                ('hyper_spectral_image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='playground.hyperspectralimage')),
                ('mask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.mask')),
            ],
        ),
    ]
