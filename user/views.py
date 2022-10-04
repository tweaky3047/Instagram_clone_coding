from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):    
    return render(request, 'home.html')


def profile_view(request):    
    return render(request, 'user/profile.html')

def sign_up(request) :
    return render(request, 'user/sign_up.html')

def sign_in(request) :
    return render(request, 'user/sign_in,html')

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