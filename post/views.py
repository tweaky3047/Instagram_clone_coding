
from django.shortcuts import render, redirect
from .models import Feed,CommentModel
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from uuid import uuid4
from insta_clone.settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required
from user.models import UserModel

# Create your views here.
# class Post()


def post_detail(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        post = Feed.objects.get(id=id)

        comments = CommentModel()
        comments.comment = comment
        comments.author = request.user
        comments.post = post
        comments.save()

        return redirect('/post/'+str(id))
    elif request.method == 'GET':
        comments = CommentModel.objects.all().order_by('-created_at')
        return render(request, 'post/post.html', {'comments': comments})

def detail_tweet(request, id):
    feed = Feed.objects.get(id=id)
    tweet_comment =CommentModel.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request,'tweet/tweet_detail.html',{'feed':feed,'comment':tweet_comment})



def delete_post(request):
    pass

@login_required
def delete_comment(request, id):
    comment = CommentModel.objects.get(id=id)
    current_feed = comment.post.id
    comment.delete()
    return redirect('/post/post/'+str(current_feed))


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
        comment = request.POST.get("input-comments","")
        current_post = Feed.objects.get(id=id)
       
        ct = CommentModel()
        ct.comment = comment
        ct.author = request.user
        ct.post = current_post
        ct.save()
        print("연결되었습니다.")
        print(comment)
        print(ct.post)
        return redirect('/post/post/'+str(id))


# @login_required
# def delete_comment(request, id):
#     if request.method == 'GET':
#         post = comment.post.id
#         comment.delete()
#         return redirect('/post/'+str(post))


def post_detail(request, id):
    feed = Feed.objects.get(id=id)
    user = UserModel.objects.get(username=feed.user_id)
    comments = CommentModel.objects.filter(post_id=id).order_by('-created_at')
    return render(request,'post/post.html',{'feed':feed,'comments':comments,'user':user})




def home_view(request) :
    feeds = Feed.objects.all()
    return render(request,'home.html',{'feeds':feeds})