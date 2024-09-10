# Generated by Django 4.2.15 on 2024-09-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_userprofile_permissions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmedicalreportmodel',
            name='custom_diagnosis',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='patientmedicalreportmodel',
            name='is_custom_diagnosis',
            field=models.BooleanField(default=False),
        ),
    ]