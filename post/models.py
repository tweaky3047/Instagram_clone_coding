from django.db import models
from user.models import UserModel
from django.contrib.auth.models import AbstractUser

class PostModel(models.Model):
    class Meta:
        db_table = "post"

    author     = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # pf_image   = models.ForeignKey('Pf_image', on_delete=models.CASCADE, upload_to='timeline_photo/%Y/%m/%d/%h/%s')
    # post_image = models.ImageField()
    text       = models.CharField(max_length=256, blank=True)
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    