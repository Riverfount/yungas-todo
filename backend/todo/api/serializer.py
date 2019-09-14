from rest_framework import serializers
from todo.api.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'deadline', 'completed_at')
