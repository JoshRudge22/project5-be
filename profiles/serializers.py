from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'bio', 'avatar', 'location', 'is_owner']

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.user if request else False