# Generated by Django 5.1.3 on 2024-11-13 01:46

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Storage', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='license_plate', unique=True)),
                ('brand', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('trailer', 'Trailer'), ('commune', 'Commune'), ('truck', 'Truck')], max_length=120)),
                ('owner', models.CharField(choices=[('company', 'Company'), ('driver', 'Driver')], max_length=120)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.driver')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.manager')),
                ('transport_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Storage.category')),
            ],
        ),
    ]
