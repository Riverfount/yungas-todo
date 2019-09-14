from rest_framework import routers
from .views import TaskViewSet

r = routers.DefaultRouter()
r.register('tasks', TaskViewSet)

urlpatterns = r.urls