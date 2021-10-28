from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models

@receiver(post_save, sender=models.WorkoutExercise)
def create_initial_set(sender, instance, created, **kwargs):
    if instance and created:
        models.Set.objects.create(workout_exercise=instance, workout=instance.workout, name='1')