from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'users'
        