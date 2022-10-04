from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_view, name='post'),
    path('post/delete/<int:id>',views.delete_post, name='delete-post'),
    path('post/<int:id>',views.post_detail, name='post-detail'),
    path('post/comment/<int:id>',views.write_comment, name='write-comment'),
    path('poast/comment/delete/<int:id>',views.delete_comment, name='delete-comment'),
]