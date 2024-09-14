from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class CommentRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
