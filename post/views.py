from django.shortcuts import render, redirect
from post.models import PostModel

from post.models import CommentModel

# Create your views here.
# class Post()
# def post_view(request):
#         return render(request, 'post/post.html')

def post_detail(request):
    return render(request, 'post/post_detail.html')

def delete_post(request):
    pass

def write_comment(request) :
    pass

def delete_comment(request) :
    pass


def post_view(request):
    if request.method == 'GET': 
        user = request.user.is_authenticated 
        if user:  
            all_post = PostModel.objects.all().order_by('-created_at')
            return render(request, 'post/home.html', {'post': all_post})
        else: 
            return redirect('/sign-in')
    elif request.method == 'POST': 
        user = request.user 
        my_post = PostModel() 
        my_post.author = user 
        my_post.content = request.POST.get('post', '')  
        my_post.save()
        return redirect('/user')