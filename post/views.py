from django.shortcuts import render
from post.models import PostModel

# Create your views here.
# class Post()
def post_view(request):
        return render(request, 'post/post.html')

def post_detail(request):
    return render(request, 'post/post_detail.html')

def delete_post(request):
    pass

def write_comment(request) :
    pass

def delete_comment(request) :
    pass