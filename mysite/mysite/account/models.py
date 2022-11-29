from django.db import models

class User(models.Model):
    fullName = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    phoneNumber = models.CharField(max_length=11, blank=False, null=False)

