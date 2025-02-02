# Generated by Django 4.2.15 on 2024-09-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_patientvistormodel_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalreportmodel',
            name='oxygen',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientmedicalreportmodel',
            name='pressure',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patientmedicalreportmodel',
            name='pulse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientmedicalreportmodel',
            name='sugar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
