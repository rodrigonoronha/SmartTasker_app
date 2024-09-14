from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from subtasks.models import SubTask
from subtasks.serializers import SubtaskSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class SubtaskListCreateAPIView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubtaskSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class SubtaskRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubtaskSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
