from .models import CommentModel, PostModel,Feed
from django.contrib import admin

admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(Feed)

