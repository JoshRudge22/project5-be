from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Goal(models.Model):
    GOAL_CHOICES = [
        ('SLIM', 'Slim Down'),
        ('MUSCLE', 'Build Muscle'),
        ('FITNESS', 'Improve Fitness'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=100)
    goal_type = models.CharField(max_length=10, choices=GOAL_CHOICES)
    target_date = models.DateField()
    progress = models.FloatField(default=0.0, help_text="Progress percentage")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.goal_type}) - {self.user.username}"

    @property
    def days_left(self):
        return (self.target_date - date.today()).days

class MiniTarget(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='mini_targets')
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"MiniTarget: {self.description} for {self.goal.title}"