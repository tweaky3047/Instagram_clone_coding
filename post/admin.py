from django.contrib import admin
from .models import PostModel,Feed

# Register your models here.
admin.site.register(PostModel)
admin.site.register(Feed)