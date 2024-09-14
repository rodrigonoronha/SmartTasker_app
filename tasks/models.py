from django.db import models
from categories.models import Category
from projects.models import Project


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, models.CASCADE, related_name='tasks')
    task_category = models.ForeignKey(Category, models.PROTECT, related_name='tasks')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
