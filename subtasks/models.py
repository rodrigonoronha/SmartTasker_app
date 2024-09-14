from django.db import models
from tasks.models import Task


class SubTask(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
# Verificar se precisa adicionar o campo created_at para ordenar os nomes criados

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
