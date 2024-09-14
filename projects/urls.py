from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ProjectListCreateAPIView.as_view(), name='project-list-create-api-view'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDeleteAPIView.as_view(), name='project-detail-api-view')
]
