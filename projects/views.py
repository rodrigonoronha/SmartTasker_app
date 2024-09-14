from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class ProjectRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
