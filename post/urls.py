from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('post/delete/<int:id>/',views.delete_post, name='delete-post'),
    path('post/<int:id>/',views.post_detail, name='post-detail'),
    path('post/comment/<int:id>',views.upload_comment, name='upload_comment'),
    path('post/comment/delete/<int:id>/',views.delete_comment, name='delete-comment'),
    path('post/upload/', views.UploadFeed.as_view()),
]