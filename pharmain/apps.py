from django.apps import AppConfig

class PharmainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pharmain'

    def ready(self):
        import pharmain.signals
