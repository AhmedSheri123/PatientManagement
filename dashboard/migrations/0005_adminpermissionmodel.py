# Generated by Django 4.2.15 on 2024-09-03 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_uploadimagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='هل المسؤول مفعل')),
                ('show_patient', models.BooleanField(default=False, verbose_name='إظهار_الجنسية')),
                ('add_patient', models.BooleanField(default=False, verbose_name='إضافة_جنسية')),
                ('delete_patient', models.BooleanField(default=False, verbose_name='حذف_الجنسية')),
                ('edit_patient', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('show_normal_visit', models.BooleanField(default=False, verbose_name='إظهار_الجنسية')),
                ('add_normal_visit', models.BooleanField(default=False, verbose_name='إضافة_جنسية')),
                ('delete_normal_visit', models.BooleanField(default=False, verbose_name='حذف_الجنسية')),
                ('edit_normal_visit', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('show_home_visit', models.BooleanField(default=False, verbose_name='إظهار_الجنسية')),
                ('add_home_visit', models.BooleanField(default=False, verbose_name='إضافة_جنسية')),
                ('delete_home_visit', models.BooleanField(default=False, verbose_name='حذف_الجنسية')),
                ('edit_home_visit', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('show_customize_medical_tests', models.BooleanField(default=False, verbose_name='إظهار_الجنسية')),
                ('add_customize_medical_tests', models.BooleanField(default=False, verbose_name='إضافة_جنسية')),
                ('delete_customize_medical_tests', models.BooleanField(default=False, verbose_name='حذف_الجنسية')),
                ('edit_customize_medical_tests', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('show_medical_tests', models.BooleanField(default=False, verbose_name='إظهار_الجنسية')),
                ('add_medical_tests', models.BooleanField(default=False, verbose_name='إضافة_جنسية')),
                ('delete_medical_tests', models.BooleanField(default=False, verbose_name='حذف_الجنسية')),
                ('edit_medical_tests', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('download_medical_tests', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('show_visit_medical_report', models.BooleanField(default=False, verbose_name='إظهار_الجنسية')),
                ('add_visit_medical_report', models.BooleanField(default=False, verbose_name='إضافة_جنسية')),
                ('delete_visit_medical_report', models.BooleanField(default=False, verbose_name='حذف_الجنسية')),
                ('edit_visit_medical_report', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('download_visit_medical_report', models.BooleanField(default=False, verbose_name='تعديل_الجنسية')),
                ('edit_settings', models.BooleanField(default=False, verbose_name='تعديل الإعدادات')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المستخدم')),
            ],
        ),
    ]
