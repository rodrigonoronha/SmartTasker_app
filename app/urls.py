
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('categories.urls')),
    path('api/v1/', include('projects.urls')),
    path('api/v1/', include('comments.urls')),
    path('api/v1/', include('tasks.urls')),
    path('api/v1/', include('subtasks.urls')),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('ai.urls')),
]
