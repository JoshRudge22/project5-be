from rest_framework import generics, permissions
from .models import Goal, MiniTarget
from .serializers import GoalSerializer, MiniTargetSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class GoalListCreateView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class MiniTargetListCreateView(generics.ListCreateAPIView):
    queryset = MiniTarget.objects.all()
    serializer_class = MiniTargetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        goal_id = self.request.data.get('goal')
        goal = Goal.objects.get(id=goal_id)
        if goal.user != self.request.user:
            raise PermissionDenied("You are not allowed to add mini-targets to this goal.")
        serializer.save(goal=goal)

class MiniTargetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MiniTarget.objects.all()
    serializer_class = MiniTargetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]