from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Follow
from .serializers import FollowSerializer
from django.contrib.auth.models import User

class FollowUserView(generics.CreateAPIView):
    """
    Allows a user to follow another user.
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class UnfollowUserView(generics.DestroyAPIView):
    """
    Allows a user to unfollow another user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user, followed=self.kwargs['username'])

    def delete(self, request, *args, **kwargs):
        follow = self.get_queryset().first()
        if follow:
            follow.delete()
            return Response({'message': 'Unfollowed successfully'}, status=204)
        return Response({'error': 'Follow relationship not found'}, status=404)

class ListFollowersView(generics.ListAPIView):
    """
    List all followers of a user.
    """
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Follow.objects.filter(followed=user)

class ListFollowingView(generics.ListAPIView):
    """
    List all users a user is following.
    """
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return Follow.objects.filter(follower=user)