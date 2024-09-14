from django.contrib import admin
from projects import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'description', 'due_date', 'project_category')
    search_fields = ('name', 'priority', 'project_category')


admin.site.register(models.Project, ProjectAdmin)
