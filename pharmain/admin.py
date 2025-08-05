from django.contrib import admin
from .models import ActivityLog

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'timestamp')
    search_fields = ('user__username', 'action', 'timestamp')
    list_filter = ('action', 'timestamp')
