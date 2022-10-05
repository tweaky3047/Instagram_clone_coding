from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import auth
from post.models import Feed
from rest_framework.views import APIView

def post_view(request):
    user = request.user.is_authenticated  
    if request.method == 'GET':
       
        user_recommand_list = UserModel.objects.all().exclude(username=request.user.username)
        feeds = Feed.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'user_recommand_list': user_recommand_list, 'feeds':feeds})

'''class prfile(APIView):
    def get(self, request):
        user = User.objects.filter(email=email).first()

       

        feed_object_list = Feed.objects.all().order_by('-id')  # select  * from content_feed;
        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(reply_content=reply.reply_content,
                                       nickname=user.nickname))
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname,
                                  reply_list=reply_list,
                                  ))


        return render(request, "/profile.html", context = dict(feeds=feed_list, user=user))'''


def profile_view(request): 
    all_feed = Feed.objects.all().order_by('-created_at')   
    return render(request, 'user/profile.html',{'feeds':all_feed})

def sign_up(request) :
    if request.method == 'GET':

        return render(request, 'user/sign_up.html')
    elif request.method == 'POST':
        username = request.POST.get('phone_number_or_email',None)
        last_name = request.POST.get('user_name',None)
        nickname = request.POST.get('user_id',None)
        password = request.POST.get('password',None)

        
        if username == '' or password == '':
                return render(request, 'user/sign_up.html', {'error': '휴대폰 번호 또는 이메일과 비밀번호는 필수입니다.'})
        else:
            exist_user =get_user_model().objects.filter(username = username)
            if exist_user:
                    return render(request, 'user/sign_up.html',{'error': '휴대폰 번호 또는 이메일이 이미 존재합니다.'})
            else:       
                new_user = UserModel()
                new_user.username = username
                new_user.last_name = last_name
                new_user.nickname = nickname
                new_user.password = password
                new_user.save()
                return redirect('/sign_in')


def sign_in_view(request):
    if request.method == 'POST':
        
        username = request.POST.get('phone_number_or_email','')
        password = request.POST.get('password','')
     
        me = UserModel.objects.get(username=username) # 사용자 불러오기
        if me.password == password:  
            auth.login(request, me)       
            request.session['user'] = me.username            
            return redirect('/home')
        else: 
            return render(request,'user/sign_in.html',{'error':'이메일 혹은 패스워드를 확인 해 주세요'}) 
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            return render(request,'user/sign_in.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/sign_in')

@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})
    
@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')