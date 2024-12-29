from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileList.as_view()),
    path('profiles/', views.ProfileDetail.as_view()),
]