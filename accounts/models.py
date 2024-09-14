from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math
import string
import random, json
from .fields import GenderFields
from .libs import DatetimeNow, when_published
from django.conf import settings
from dashboard.models import AdminPermissionModel

BASE_DIR = settings.BASE_DIR
# Create your models here.

account_type_choices = (
    ('0', 'מנהל'),
    ('2', 'פקיד'),
    ('3', 'מטופל'),
)

account_alias_name_choices = (
    ('0', 'פקיד'),
    ('2', 'طبيب'),
    ('3', 'לבורנט'),
)

visit_distance_choices = (
    ('1', '0-30 KM'),
    ('2', '30-60 KM'),
)

def CompanyRandomNumCodeGen():
    N = 5
    res = ''.join(random.choices(string.digits, k=N))
    return 'p' + str(res)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    patient_profile = models.ForeignKey('PatientProfile', on_delete=models.CASCADE, null=True, blank=True)
    permissions = models.ForeignKey(AdminPermissionModel, on_delete=models.SET_NULL, null=True, blank=True)

    profile_type = models.CharField(max_length=255, choices = account_type_choices, null=True, blank=True, verbose_name="نوع الملف الشخصي")
    account_alias_name = models.CharField(max_length=255, choices = account_alias_name_choices, null=True, blank=True, verbose_name="اسم المستعار للملف الشخصي")
    
    phone = models.CharField(max_length=255, verbose_name='رقم الهاتف')
    address = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, choices=GenderFields, null=True, blank=True, verbose_name='الجنس')
    id_number = models.IntegerField(null=True, verbose_name="العمر")
    birth_date = models.DateField(null=True, verbose_name="العمر")

    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

    def __str__(self):
        return self.user.username
    

class PatientProfile(models.Model):
    id_number = models.IntegerField(null=True, verbose_name="العمر")
    birth_date = models.DateField(null=True, verbose_name="العمر")
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")
    # def __str__(self):
    #     return self.name

class PatientVistorModel(models.Model):
    user = models.ForeignKey(User, related_name='vistor_patient', null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor', null=True, on_delete=models.CASCADE)

    visitor_pay_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0.00)
    is_home_visit = models.BooleanField(default=False)
    visit_distance = models.CharField(max_length=254, choices=visit_distance_choices, null=True, blank=True)

    note = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")
    # def __str__(self):
    #     return self.name

    def whenpublished(self):
        return when_published(self.creation_date)

class PatientMedicalReportModel(models.Model):
    vistor = models.ForeignKey(PatientVistorModel, related_name='vistor', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='vistor_doctor', on_delete=models.CASCADE)
    reason_for_visit = models.TextField()

    pulse = models.IntegerField(blank=True, null=True)
    pressure = models.CharField(max_length=255, blank=True, null=True)
    oxygen = models.IntegerField(blank=True, null=True)
    sugar = models.IntegerField(blank=True, null=True)

    clinical_examination = models.TextField()
    treatment = models.TextField()
    diagnosis = models.CharField(max_length=254)
    is_custom_diagnosis = models.BooleanField(default=False)
    custom_diagnosis = models.CharField(max_length=254, blank=True, null=True, default='')


    recommendations = models.TextField()

    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")
    # def __str__(self):
    #     return self.name

    def whenpublished(self):
        return when_published(self.creation_date)
    
    def get_diagnosis(self):
        file = open(str(BASE_DIR / 'accounts/diagnosis_codes3.json'), 'r').read()
        diagnosises = json.loads(file)
        for i in diagnosises:
            if i.get('code') == self.diagnosis:
                return i.get('descr')
        return ''