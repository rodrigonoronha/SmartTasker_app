from django.contrib import admin
from tasks import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date', 'project', 'task_category')
    search_fields = ('name', 'project', 'task_category')


admin.site.register(models.Task, TaskAdmin)
