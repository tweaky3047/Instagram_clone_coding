from django.shortcuts import render
from post.models import PostModel,Feed
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import CommentModel
import os
from uuid import uuid4
from insta_clone.settings import MEDIA_ROOT
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

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        
        image =  uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image = image, content=content, user_id=user_id, profile_image=profile_image)

       

        return Response(status=200)
