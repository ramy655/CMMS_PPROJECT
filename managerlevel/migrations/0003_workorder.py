# Generated by Django 3.1.4 on 2021-02-02 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managerlevel', '0002_medicaldevice_department_of_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Case', models.BooleanField(max_length=250)),
                ('Time_Response', models.TimeField(blank=True, null=True)),
                ('Assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('Department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='managerlevel.departments')),
                ('Equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='managerlevel.medicaldevice')),
            ],
        ),
    ]