from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.TaskListCreateAPIView.as_view(), name='task-list-create-api-view'),
    path('tasks/<int:pk>/', views.RetrieveUpdateDeleteAPIView.as_view(), name='task-detail-api-view'),
]
