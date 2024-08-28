# Generated by Django 5.1 on 2024-08-28 05:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=100)),
                ('line2', models.CharField(blank=True, max_length=100)),
                ('line3', models.CharField(blank=True, max_length=100)),
                ('line4', models.CharField(blank=True, max_length=100)),
                ('line5', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('contact_first_name', models.CharField(max_length=50)),
                ('contact_last_name', models.CharField(max_length=50)),
                ('employees', models.CharField(max_length=20)),
                ('business_focus', models.CharField(max_length=20)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
