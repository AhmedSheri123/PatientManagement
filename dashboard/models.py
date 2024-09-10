from django.db import models
from django.contrib.auth.models import User
from accounts.libs import when_published
# Create your models here.

class CustomizeMedicalTestsModel(models.Model):
    name = models.CharField(max_length=254, null=True)
    data = models.JSONField(null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")


    def whenpublished(self):
        return when_published(self.creation_date)

class MedicalTestsModel(models.Model):
    patient = models.ForeignKey(User, related_name='patient_test', null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor_test', null=True, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=254, null=True)
    data = models.JSONField(null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")


    def whenpublished(self):
        return when_published(self.creation_date)
    
class UploadImageModel(models.Model):
    img = models.ImageField(upload_to='img/%Y/%m')
    img_base64 = models.TextField()


class AdminPermissionModel(models.Model):
    is_enabled = models.BooleanField(default=True, verbose_name='هل المسؤول مفعل')

    show_index = models.BooleanField(default=False, verbose_name='ادارة اللوحة الرئيسية')

    # أذونات المرضى
    show_patient = models.BooleanField(default=False, verbose_name='ادارة المرضى')
    add_patient = models.BooleanField(default=False, verbose_name='إضافة مريض')
    delete_patient = models.BooleanField(default=False, verbose_name='حذف مريض')
    edit_patient = models.BooleanField(default=False, verbose_name='تعديل مريض')

    # أذونات الزيارات العادية
    show_normal_visit = models.BooleanField(default=False, verbose_name='ادارة الزيارات العادية')
    add_normal_visit = models.BooleanField(default=False, verbose_name='إضافة زيارة عادية')
    delete_normal_visit = models.BooleanField(default=False, verbose_name='حذف زيارة عادية')
    edit_normal_visit = models.BooleanField(default=False, verbose_name='تعديل زيارة عادية')

    # أذونات الزيارات المنزلية
    show_home_visit = models.BooleanField(default=False, verbose_name='ادارة الزيارات المنزلية')
    add_home_visit = models.BooleanField(default=False, verbose_name='إضافة زيارة منزلية')
    delete_home_visit = models.BooleanField(default=False, verbose_name='حذف زيارة منزلية')
    edit_home_visit = models.BooleanField(default=False, verbose_name='تعديل زيارة منزلية')

    # أذونات تخصيص الفحوصات الطبية
    show_customize_medical_tests = models.BooleanField(default=False, verbose_name='ادارة تخصيص الفحوصات الطبية')
    add_customize_medical_tests = models.BooleanField(default=False, verbose_name='إضافة تخصيص الفحوصات الطبية')
    delete_customize_medical_tests = models.BooleanField(default=False, verbose_name='حذف تخصيص الفحوصات الطبية')
    edit_customize_medical_tests = models.BooleanField(default=False, verbose_name='تعديل تخصيص الفحوصات الطبية')

    # أذونات الفحوصات الطبية
    show_medical_tests = models.BooleanField(default=False, verbose_name='ادارة الفحوصات الطبية')
    view_medical_tests = models.BooleanField(default=False, verbose_name='عرض الفحوصات الطبية')
    add_medical_tests = models.BooleanField(default=False, verbose_name='إضافة الفحوصات الطبية')
    delete_medical_tests = models.BooleanField(default=False, verbose_name='حذف الفحوصات الطبية')
    edit_medical_tests = models.BooleanField(default=False, verbose_name='تعديل الفحوصات الطبية')
    download_medical_tests = models.BooleanField(default=False, verbose_name='تحميل الفحوصات الطبية')

    # أذونات تقارير الزيارات الطبية
    show_visit_medical_report = models.BooleanField(default=False, verbose_name='ادارة تقارير الزيارات الطبية')
    view_visit_medical_report = models.BooleanField(default=False, verbose_name='عرض تقارير الزيارات الطبية')
    add_visit_medical_report = models.BooleanField(default=False, verbose_name='إضافة تقارير الزيارات الطبية')
    delete_visit_medical_report = models.BooleanField(default=False, verbose_name='حذف تقارير الزيارات الطبية')
    edit_visit_medical_report = models.BooleanField(default=False, verbose_name='تعديل تقارير الزيارات الطبية')
    download_visit_medical_report = models.BooleanField(default=False, verbose_name='تحميل تقارير الزيارات الطبية')

    edit_settings = models.BooleanField(default=False, verbose_name='تعديل الإعدادات')

