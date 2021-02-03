# Generated by Django 3.1.4 on 2021-01-25 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicaldevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('serial_number', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('manufacture', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('model_device', models.CharField(max_length=250)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
