from django.urls import path
from ai import views


urlpatterns = [
    path('ai/', views.AICommentAPIView.as_view(), name='ai-comment'),

]
