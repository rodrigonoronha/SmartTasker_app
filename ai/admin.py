from django.contrib import admin
from ai.models import AIResult


class AIAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    search_fields = ('id',)


admin.site.register(AIResult, AIAdmin)
