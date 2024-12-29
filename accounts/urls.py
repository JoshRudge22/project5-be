from django.urls import path
from . import views

urlpatterns = [
    path('follows/', views.FollowUserView.as_view(), name='follow-user'),
    path('follows/<str:username>/', views.UnfollowUserView.as_view(), name='unfollow-user'),
    path('followers/<str:username>/', views.ListFollowersView.as_view(), name='list-followers'),
    path('following/<str:username>/', views.ListFollowingView.as_view(), name='list-following'),
]