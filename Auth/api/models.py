from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,12}$', message="Phone number must be entered in the format: '999999999'. Up to 12 digits allowed.")
    phone = models.CharField(blank=True,max_length=12,validators=[phone_regex]) # validators should be a list
    username = models.SlugField(unique=True)

    class Meta:
        unique_together = ('phone', 'email',)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)