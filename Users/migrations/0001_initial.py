# Generated by Django 5.1.3 on 2024-11-13 01:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('social_security_number', models.CharField(max_length=255, unique=True)),
                ('business_field', models.CharField(blank=True, max_length=255, null=True)),
                ('wallet_balance', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('Users.customuser',),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('drive_license_id', models.CharField(max_length=255, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='driver_pictures')),
                ('debt_balance', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('travel_count', models.IntegerField(default=0)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
            bases=('Users.customuser',),
        ),
        migrations.CreateModel(
            name='MainManager',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('access_code', models.CharField(max_length=255, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures')),
                ('grand_balance', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('Users.customuser',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employee_id', models.CharField(max_length=255, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='manager_pictures')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('management_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('Users.customuser',),
        ),
        migrations.CreateModel(
            name='CustomerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='customer_images')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Users.customer')),
            ],
        ),
        migrations.CreateModel(
            name='DriverImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='driver_images')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Users.driver')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='manager_images')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('manager_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.manager')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='assigned_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='Users.manager'),
        ),
    ]
