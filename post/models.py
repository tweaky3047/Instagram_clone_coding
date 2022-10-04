from unittest.util import _MAX_LENGTH
from django.db import models
from user.models import UserModel
from django.contrib.auth.models import AbstractUser

class PostModel(models.Model):
    class Meta:
        db_table = "post"

    author     = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # pf_image   = models.ForeignKey('Pf_image', on_delete=models.CASCADE, upload_to='timeline_photo/%Y/%m/%d/%h/%s')
    # post_image = models.ImageField()
    text       = models.CharField(max_length=255, blank=True)
    # charfield의 제한이 255까지라 수정해 두었습니다.
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtag = models.CharField(max_length=30)

class CommentModel(models.Model) :
    class Meta :
        db_table = "comment"
    
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    #제가 찾은 바로는 덧글에 글자수 제한이 없어서 계획은 varchar였는데 일단은 textfield로 해놓았습니다.
    comment = models.TextField()
    #제가 못 찾은 건지 덧글 수정 기능을 찾을 수 없어 생성시時만 기록하도록 auto_now_add를 사용했습니다.
    created_at = models.DateTimeField(auto_now_add=True)