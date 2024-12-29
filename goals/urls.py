from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.GoalListCreateView.as_view(), name='goal-list'),
    path('goals/<int:pk>/', views.GoalDetailView.as_view(), name='goal-detail'),
    path('mini-targets/', views.MiniTargetListCreateView.as_view(), name='mini-target-list'),
    path('mini-targets/<int:pk>/', views.MiniTargetDetailView.as_view(), name='mini-target-detail'),
]