from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 如果要加欄位就在這裡加，例如：
    phone = models.CharField(max_length=15, blank=True)
    pass