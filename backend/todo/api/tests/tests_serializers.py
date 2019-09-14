from datetime import datetime

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from todo.api.models import Tasks


class TasksListTest(APITestCase):

    def setUp(self) -> None:
        self.data = {
            'title': 'Task',
            'description': 'My Task Description',
            'deadline': '2019-09-13',
            'completed_at': None
        }

    def test_post_task(self):
        url = '/api/v1/tasks/'
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tasks.objects.count(), 1)
        self.assertEqual(Tasks.objects.get().title, self.data['title'])

    def test_get_task_list_status_code(self):
        url = '/api/v1/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_done_tasks(self):
        url = '/api/v1/tasks/'
        resp = self.client.post(url, self.data, format='json')
        url = '/api/v1/tasks/1/done/'
        response = self.client.post(url)
        completed_at = datetime.strftime(timezone.now().date(), '%Y-%m-%d')
        self.assertEqual(response.data['completed_at'], completed_at)
