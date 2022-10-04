
from django.shortcuts import render, redirect
from post.models import PostModel

from post.models import CommentModel

# Create your views here.
# class Post()

def post_view(request):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        post = PostModel.objects.get(id=id)

        comments = CommentModel()
        comments.comment = comment
        comments.author = request.user
        comments.post = post
        comments.save()

        return redirect('/post/'+str(id))
    elif request.method == 'GET' :
        comments = CommentModel.objects.all().order_by('-created_at')
        print(comments)
        return render(request,'post/post.html',{'comments' : comments})


def post_detail(request):
    return render(request, 'post/post_detail.html')

def delete_post(request):
    pass

def write_comment(request, id) :
    pass

def delete_comment(request, id) :
    comment = CommentModel.objects.all(id=id)
    post = comment.post.id
    comment.delete()
    return redirect('/tweet/'+str(post))

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
