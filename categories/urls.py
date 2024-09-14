from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create-api-view'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDeleteAPIView.as_view(), name='category-detail-api-view'),
]
