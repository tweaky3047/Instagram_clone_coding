from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    
    class Meta:
        db_table = "my_user"

    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='timeline_photo')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')
    nickname = models.CharField(max_length=30, blank=False, null=True)

