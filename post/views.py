from django.shortcuts import redirect, render
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