from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create-api-view'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDeleteAPIView.as_view(), name='comment-detail-api-view'),
]
