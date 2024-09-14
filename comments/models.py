from django.db import models
from projects.models import Project


class Comment(models.Model):

    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, models.CASCADE, related_name='comments')
