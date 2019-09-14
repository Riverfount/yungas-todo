from todo.api.models import Tasks
from todo.api.serializer import TaskSerializer
from rest_framework import viewsets, response
from rest_framework.decorators import action
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['post'], detail=True)
    def done(self, request, pk=None):
        task = self.get_object()
        task.completed_at = timezone.now().date()
        task.save()

        return response.Response(self.get_serializer(task).data)
