from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('sign_up/', views.sign_up, name='sign-up'),
    path('user/', views.user_view, name='user-list'),
    path('user/follow/<int:id>/', views.user_follow, name='user-follow'),
    path('sign_in/',views.sign_in_view, name='sign-in'),
    path('logout/',views.logout, name='logout'),
]