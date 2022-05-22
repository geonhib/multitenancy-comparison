from django.db import models
from django_scopes import ScopedManager
from django.contrib.auth import get_user_model
User = get_user_model()


TENANT_STATUS = (
    ('active','active'),
    ('inactive','inaactive'),
)
class Site(models.Model):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=TENANT_STATUS, default='inactive')

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)

    objects = ScopedManager(site='site')

    def __str__(self) -> str:
        return f"{self.site } - {self.name}"


class Program(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    objects = ScopedManager(site='department__site')

    def __str__(self) -> str:
        return self.text


# class intructor(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)

#     objects = ScopedManager(site='post__site')

#     def __str__(self) -> str:
#         return self.text