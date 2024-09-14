from django.contrib import admin
from subtasks import models


class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task')
    search_fields = ('name',)


admin.site.register(models.SubTask, SubtaskAdmin)
