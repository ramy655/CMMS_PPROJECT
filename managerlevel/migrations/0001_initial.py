# Generated by Django 3.1.4 on 2021-01-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Medicaldevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('serial_number', models.CharField(max_length=250)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('manufacture', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('model_device', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]