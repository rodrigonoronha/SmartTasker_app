from django.db import models
from categories.models import Category

PRIORITIES = (
    ('High', "H"),
    ('Medium', "M"),
    ('Low', "L"),
)


class Project(models.Model):
    name = models.CharField(max_length=50)
    priority = models.CharField(max_length=6, choices=PRIORITIES)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    project_category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='projects')

    class Meta:

        ordering = ['created_at']

    def __str__(self):
        return self.name
