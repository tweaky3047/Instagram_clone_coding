from django.contrib import admin
from .models import CommentModel, Image, PostModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(Image)
admin.site.register(CommentModel)