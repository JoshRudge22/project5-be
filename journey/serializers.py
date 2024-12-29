from rest_framework import serializers
from .models import Journey, Like

class JourneySerializer(serializers.ModelSerializer):
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = Journey
        fields = ['id', 'user', 'title', 'content', 'created_at', 'public', 'week_number', 'like_count']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'journey', 'created_at']
        read_only_fields = ['user', 'created_at']