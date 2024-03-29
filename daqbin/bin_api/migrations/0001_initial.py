# Generated by Django 5.0.1 on 2024-01-16 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('binId', models.AutoField(primary_key=True, serialize=False)),
                ('binUniqueId', models.CharField(max_length=10)),
                ('binSize', models.CharField(max_length=10)),
                ('manufactureDate', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BinData',
            fields=[
                ('binDataId', models.AutoField(primary_key=True, serialize=False)),
                ('binLevel', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=20)),
                ('binTemperaure', models.CharField(max_length=20)),
                ('binOrientation', models.CharField(max_length=20)),
                ('_bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bin_api.bin')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('assignedBin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bin_api.bin')),
            ],
        ),
    ]
