from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from categories.models import Category
from . import serializers
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class CategoryRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
