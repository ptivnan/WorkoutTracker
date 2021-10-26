from django.db import models
from django.urls import reverse


class Workout(models.Model):
    date =  models.DateField(auto_now_add=True)
    name = models.CharField(max_length=64, blank=False, null=False)
    notes = models.TextField(blank=True, null=True)
    complete = models.BooleanField(null=False, default=False)

    def get_absolute_url(self):
        return reverse('workout-detail', kwargs={'id': self.id})

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('workout-exercise-detail', kwargs={'id': self.id})

class Set(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default="Set")
    workout = models.ForeignKey(Workout, blank=True, null=True, on_delete=models.CASCADE)
    workout_exercise = models.ForeignKey(WorkoutExercise, blank=True, null=True, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    reps = models.PositiveSmallIntegerField(blank=True, null=True)
    failure = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name
