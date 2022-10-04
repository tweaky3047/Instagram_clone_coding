from django.shortcuts import render

# Create your views here.
def home_view(request):    
    return render(request, 'home.html')


def profile_view(request):    
    return render(request, 'user/profile.html')

def sign_up(request) :
    return render(request, 'user/sign_up.html')

def sign_in(request) :
    return render(request, 'user/sign_in,html')

