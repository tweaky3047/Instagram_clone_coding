from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('sign_up/', views.sign_up, name='sign-up'),
    path('sign_in/',views.sign_in, name='sign-in'),
]