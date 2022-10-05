
from django.shortcuts import render, redirect
from post.models import PostModel, Feed
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import CommentModel
import os
from uuid import uuid4
from insta_clone.settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required

# Create your views here.
# class Post()


def post_detail(request):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        post = PostModel.objects.get(id=id)

        comments = CommentModel()
        comments.comment = comment
        comments.author = request.user
        comments.post = post
        comments.save()

        return redirect('/post/'+str(id))
    elif request.method == 'GET':
        comments = CommentModel.objects.all().order_by('-created_at')
        return render(request, 'post/post.html', {'comments': comments})


# def post_detail(request):
#     return render(request, 'post/post_detail.html')

def delete_post(request):
    pass


def write_comment(request, id):
    pass


def delete_comment(request):
    pass


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        user_id = request.user.username
        profile_image = request.user.profile_image

        Feed.objects.create(image=image, content=content,
                            user_id=user_id, profile_image=profile_image)

        return Response(status=200)


@login_required
def upload_comment(request, id):
    if request.method == 'POST':
        comment = CommentModel.objects.all(id=id)
        post = comment.post.id
        comment.put()
        return redirect('/post/'+str(id=id))


@login_required
def delete_comment(request, id):
    if request.method == 'POST':
        comment = CommentModel.objects.all(id=id)
        post = comment.post.id
        comment.delete()
        return redirect('/post/'+str(post))


def post_detaild(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_post = PostModel.objects.all().order_by('-created_at')
            return render(request, 'post/post.html', {'post': all_post})
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user
        my_post = PostModel()
        my_post.author = user
        my_post.content = request.POST.get('post', '')
        my_post.save()
        return redirect('/user')




def home_view(request) :
    feeds = Feed.objects.all()
    return render(request,'home.html',{'feeds':feeds})