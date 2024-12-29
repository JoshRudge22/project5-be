from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Journey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journeys')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    week_number = models.IntegerField(default=datetime.now().isocalendar()[1])

    def __str__(self):
        return f"{self.title} by {self.user.username}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('user', 'journey')

@property
def like_count(self):
    return self.likes.count()

    def __str__(self):
        return f"{self.user.username} liked {self.journey.title}"