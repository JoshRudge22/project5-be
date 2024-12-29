from django.urls import path
from .views import EditProfileView, ResourceListView, InquiryCreateView

urlpatterns = [
    path('profile/edit/', EditProfileView.as_view()),
    path('resources/', ResourceListView.as_view()),
    path('inquiry/', InquiryCreateView.as_view())
]