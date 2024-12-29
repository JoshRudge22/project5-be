from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Journey, Like
from .serializers import JourneySerializer, LikeSerializer
from drf_api.permissions import IsOwnerOrReadOnly


# List all public journeys or create a new one
class JourneyListCreateView(generics.ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter journeys based on public visibility
        return Journey.objects.filter(public=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve, update, or delete a journey
class JourneyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# Toggle Like for a journey
class LikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, journey_id):
        try:
            journey = Journey.objects.get(id=journey_id)
        except Journey.DoesNotExist:
            return Response({"error": "Journey not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user already liked the journey
        like, created = Like.objects.get_or_create(user=request.user, journey=journey)

        if not created:  # If the user already liked it, remove the like
            like.delete()
            return Response({"message": "Like removed."}, status=status.HTTP_200_OK)

        return Response({"message": "Journey liked!"}, status=status.HTTP_201_CREATED)


# List users who liked a specific journey
class JourneyLikersView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        journey_id = self.kwargs['journey_id']
        return Like.objects.filter(journey__id=journey_id)


# List journeys sorted by most likes
class JourneyMostLikedView(generics.ListAPIView):
    serializer_class = JourneySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Journey.objects.annotate(like_count=Count('likes')).order_by('-like_count')