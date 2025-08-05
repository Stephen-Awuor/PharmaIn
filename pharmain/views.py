from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import ActivityLog

@staff_member_required
def activity_log_view(request):
    logs = ActivityLog.objects.all().order_by('-timestamp')[:200]
    return render(request, 'pharmain/activity_log.html', {'logs': logs})
