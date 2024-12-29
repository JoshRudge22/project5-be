from django.contrib import admin
from .models import Goal, MiniTarget

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'goal_type', 'user', 'target_date', 'progress', 'created_at')

@admin.register(MiniTarget)
class MiniTargetAdmin(admin.ModelAdmin):
    list_display = ('description', 'goal', 'completed')