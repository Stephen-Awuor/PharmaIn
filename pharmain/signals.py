from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from pharmain.models import ActivityLog
from sales.models import Sale


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ActivityLog.objects.create(user=user, action='LOGIN', description='User logged in')

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ActivityLog.objects.create(user=user, action='LOGOUT', description='User logged out')

@receiver(post_save, sender=Sale)
def log_sale_change(sender, instance, created, **kwargs):
    user = getattr(instance, 'created_by', None)
    ActivityLog.objects.create(
        user=user,
        action='CREATE' if created else 'UPDATE',
        description=f"Sale #{instance.id} {'created' if created else 'updated'}"
    )

@receiver(post_delete, sender=Sale)
def log_sale_deleted(sender, instance, **kwargs):
    user = getattr(instance, 'created_by', None)
    ActivityLog.objects.create(
        user=user,
        action='DELETE',
        description=f"Sale #{instance.id} deleted"
    )
