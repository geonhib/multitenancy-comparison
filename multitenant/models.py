from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

from django_multitenant.fields import *
from django_multitenant.models import *


TENANT_STATUS = (
    ('active', 'active'),
    ('inaactive', 'inactive'),
)
class School(TenantModel):
    tenant_id = 'id'
    name = models.CharField(max_length=80)
    status = models.CharField(max_length=30, choices=TENANT_STATUS, default='inactive')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(TenantModel):
    tenant_id = 'school_id'
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} - {self.school}"

    class Meta:
        unique_together = ['id', 'school', ]


class Program(TenantModel):
    tenant_id = 'school_id'
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    department = TenantForeignKey(Department, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.activity}"
