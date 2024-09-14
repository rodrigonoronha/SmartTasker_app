from django.contrib import admin
from comments import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'project')
    search_fields = ('project',)


admin.site.register(models.Comment, CommentAdmin)
