# Generated by Django 4.2.15 on 2024-08-29 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_alter_patientmedicalreportmodel_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientvistormodel',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patientvistormodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vistor_patient', to=settings.AUTH_USER_MODEL),
        ),
    ]