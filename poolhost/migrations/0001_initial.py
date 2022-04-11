# Generated by Django 4.0.3 on 2022-03-24 06:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('siteadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiclename', models.CharField(max_length=30)),
                ('brandname', models.CharField(max_length=30)),
                ('vehicle_image', models.ImageField(blank=True, null=True, upload_to='vehicle_image')),
                ('number_plate', models.ImageField(blank=True, null=True, upload_to='number_plate')),
                ('rc_image', models.ImageField(blank=True, null=True, upload_to='rc_image')),
                ('fuel_type', models.CharField(max_length=20)),
                ('capacity', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{2}$')])),
                ('fuel_capacity', models.CharField(max_length=2)),
                ('Vehical_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.vehicaltype')),
            ],
        ),
    ]
