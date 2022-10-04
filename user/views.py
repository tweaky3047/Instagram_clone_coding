from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth.decorators import login_required
import re
from django.contrib.auth import get_user_model



# Create your views here.
def home_view(request):    
    return render(request, 'home.html')


def profile_view(request):    
    return render(request, 'user/profile.html')

def sign_up(request) :
    if request.method == 'GET':

        return render(request, 'user/sign_up.html')
    elif request.method == 'POST':
        email = request.POST.get('phone_number_or_email',None)
        username = request.POST.get('user_name',None)
        nickname = request.POST.get('user_id',None)
        password = request.POST.get('password',None)

        
        if email == '' or password == '':
                return render(request, 'user/sign_up.html', {'error': '휴대폰 번호 또는 이메일과 비밀번호는 필수입니다.'})
        else:
            exist_user =get_user_model().objects.filter(email = email)
            if exist_user:
                    return render(request, 'user/sign_up.html',{'error': '휴대폰 번호 또는 이메일이 이미 존재합니다.'})
            else:       
                new_user = UserModel()
                new_user.email = email
                new_user.username = username
                new_user.nickname = nickname
                new_user.password = password
                new_user.save()
                return redirect('/sign_in')


def sign_in(request) :
    return render(request, 'user/sign_in.html')

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