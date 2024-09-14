from django.urls import path
from . import views


urlpatterns = [
    path('subtasks/', views.SubtaskListCreateAPIView.as_view(), name="subtask-list-create-api-view"),
    path('subtasks/<int:pk>/', views.SubtaskRetrieveUpdateDeleteAPIView.as_view(), name="subtask-detail-api-view"),
]
