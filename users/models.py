from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    phone = models.CharField(max_length=50, verbose_name='number of phone')
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar')
    country = models.CharField(max_length=100, verbose_name='country')
    email_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
