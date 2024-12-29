from django.urls import path
from . import views

urlpatterns = [
    path('', views.JourneyListCreateView.as_view()),
    path('journeys/<int:pk>/', views.JourneyDetailView.as_view()),
    path('journeys/<int:journey_id>/like/', views.LikeToggleView.as_view()),
    path('journeys/<int:journey_id>/likers/', views.JourneyLikersView.as_view()),
    path('journeys/most-liked/', views.JourneyMostLikedView.as_view()),
]