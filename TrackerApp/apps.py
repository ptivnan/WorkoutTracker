from django.apps import AppConfig


class TrackerappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TrackerApp'

    def ready(self):
        from django.db.models.signals import post_save
        from .signals import create_initial_set
        from .models import WorkoutExercise
        post_save.connect(create_initial_set, sender=WorkoutExercise)