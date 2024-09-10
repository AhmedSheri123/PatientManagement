from django import template
# from accounts.models import CompanyCreateJobModel, EmployeeJobRequest
import json
from django.conf import settings
from dashboard.libs import has_permission
from accounts.models import PatientMedicalReportModel
register = template.Library()

@register.simple_tag
def temp_get_permission_state(user_id, action, resource):
    p = has_permission(user_id, action, resource)
    
    return p

@register.simple_tag
def get_visit_medical_reports(visit_id):
    reports = PatientMedicalReportModel.objects.filter(vistor__id=visit_id)    
    return reports

# @register.simple_tag
# def NumberOfPresenters(job_id):
#     presenters = EmployeeJobRequest.objects.filter(company_job__id=job_id)
#     count = str(presenters.count())
#     return count

# @register.simple_tag
# def AcceptedOfPresenters(job_id):
#     presenters = EmployeeJobRequest.objects.filter(post_state='3', company_job__id=job_id)
#     count = str(presenters.count())
#     return count


# @register.simple_tag
# def GenFooter(job_id):
#     html = open(settings.BASE_DIR / 'media/footer.json', 'r', encoding='utf-8').read()
#     loaded = json.loads(html)
#     return loaded