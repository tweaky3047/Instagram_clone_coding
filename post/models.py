from django.db import models
from user.models import UserModel


class Feed(models.Model):
    
    content = models.TextField()   
    image = models.TextField()  
    profile_image = models.TextField()
    user_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True, ) 
    

       
class CommentModel(models.Model) :
    class Meta :
        db_table = "comment"
    
    post = models.ForeignKey(Feed, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)