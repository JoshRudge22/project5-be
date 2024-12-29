from rest_framework import serializers
from .models import Resource, Inquiry

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'url', 'type', 'description']

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'user', 'subject', 'message', 'created_at', 'resolved']