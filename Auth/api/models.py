from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,12}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    phone = models.CharField( blank=True,max_length=12) # validators should be a list
    