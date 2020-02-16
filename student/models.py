from django.db import models
from django.db.models.signals import post_save

class UsersAccount(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.username
