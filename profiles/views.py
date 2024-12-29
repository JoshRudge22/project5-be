from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from drf_api.permissions import IsOwnerOrReadOnly

class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        try:
            return self.queryset.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise NotFound("Profile not found.")

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]