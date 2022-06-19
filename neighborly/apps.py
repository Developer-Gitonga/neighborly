from django.apps import AppConfig


class NeighborlyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'neighborly'

    def ready(self):
        import neighborly.signals