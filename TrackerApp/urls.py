from django.urls import path
from . import views


urlpatterns = [
    path('', views.TrackerHome, name='tracker-home'),
    path('workout/<str:id>', views.WorkoutDetail, name='workout-detail'),
    path('workout/exercise/<str:id>', views.WorkoutExerciseDetail, name='workout-exercise-detail'),
]