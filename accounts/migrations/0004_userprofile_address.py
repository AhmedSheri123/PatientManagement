# Generated by Django 4.2.15 on 2024-08-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_birth_date_userprofile_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]