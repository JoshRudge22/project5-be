from rest_framework import serializers
from .models import Goal, MiniTarget

class MiniTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniTarget
        fields = ['id', 'description', 'completed']

class GoalSerializer(serializers.ModelSerializer):
    mini_targets = MiniTargetSerializer(many=True, read_only=True)
    days_left = serializers.ReadOnlyField()

    class Meta:
        model = Goal
        fields = [
            'id', 'title', 'goal_type', 'target_date', 'progress',
            'created_at', 'days_left', 'mini_targets',
        ]