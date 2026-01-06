from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Extended User model with fullname field"""
    fullname = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username


