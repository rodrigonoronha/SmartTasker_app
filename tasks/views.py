from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class RetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
