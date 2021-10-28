from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from . import forms, models
from django.db.models import Count

def TrackerHome(request):
    #Vars
    workouts = models.Workout.objects.filter(complete=False).order_by('-date')
    exercises = models.Exercise.objects.all().order_by('name')

    #Forms
    WorkoutForm = forms.WorkoutForm(request.POST or None)
    ExerciseForm = forms.ExerciseForm(request.POST or None)

    #Handle form submission
    if request.method == 'POST':
        if 'create-workout' in request.POST:
            print(f"WorkoutForm valid: ", WorkoutForm.is_valid())
            print(f"WorkoutForm errors: ", WorkoutForm.errors.as_data())
            if WorkoutForm.is_valid():
                new_workout = WorkoutForm.save()
                return redirect(new_workout)

        elif 'create-exercise' in request.POST:
            print(f"ExerciseForm valid: ", ExerciseForm.is_valid())
            print(f"ExerviceForm errors: ", ExerciseForm.errors.as_data())
            if ExerciseForm.is_valid():
                ExerciseForm.save()

        return redirect('tracker-home')

    context = {
        'workoutform': WorkoutForm,
        'exerciseform': ExerciseForm,
        'workouts': workouts,
        'exercises': exercises,
    }
    return render(request, "trackerapp/home.html", context)

def WorkoutDetail(request, **kwargs):
    id = kwargs.get('id')
    workout = get_object_or_404(models.Workout, id=id)
    workout_exercise_list = models.WorkoutExercise.objects.filter(workout=workout)
    exercise_set_list = models.Set.objects.filter(workout=workout)
    workout_form = forms.WorkoutForm(request.POST or None, instance=workout)
    workout_exercise_form = forms.WorkoutExerciseForm(request.POST or None, initial={'workout': workout})
    workout_exercise_list_form = forms.WorkoutExerciseListForm()
    sets = models.Set.objects.filter(workout=workout)
    workout_exercise_set_count = models.Set.objects.values('workout_exercise').annotate(sets=Count('workout_exercise'))
    number_of_sets = f"{len(sets) + 1}"
    formset = forms.WorkoutFormset(request.POST or None, instance=workout, initial=[{'name': "test", 'workout': workout}])
    set_form = forms.SetForm(request.POST or None, initial={'workout': workout})
    #print(workout_exercise_set_count)
    print(number_of_sets)
    #print(models.Set.objects.filter(workout=workout).count())

    #print(workout['sets'] for workout in workout_exercise_set_count)


    context = {
        'workout': workout,
        'workout_exercise': workout_exercise_form,
        'workout_exercise_list': workout_exercise_list,
        'workout_exercise_list_form': workout_exercise_list_form,
        'exercise_set_list': exercise_set_list, 
        'all_sets': models.Set.objects.all(),
        'workout_form': workout_form, 
        'id': id,
        'formset': formset,
        'set_form': set_form,
        'workout_exercise_set_count': workout_exercise_set_count,

    }

    if request.method == 'POST':

        if 'update-workout' in request.POST:
            print(f"form valid: ", workout_form.is_valid())
            print(f"Form errors: ", workout_form.errors.as_data())
            if workout_form.is_valid():
                workout_form.save()
                return redirect(workout)

        elif 'add-exercise' in request.POST:
            print(f"workout_exercise valid: ", workout_exercise_form.is_valid())
            print(f"workout_exercise errors", workout_exercise_form.errors.as_data())
            if workout_exercise_form.is_valid():
                exercise = workout_exercise_form.save(commit=False)
                exercise.workout = workout
                exercise.save()
                return redirect(workout)

        elif 'delete-workout-exercise' in request.POST:
            print(f"Request to delete workout exercise")
            for i in request.POST.getlist('delete-exercise'):
                exercise = models.WorkoutExercise.objects.get(id=i)
                exercise.delete()
                return redirect(workout)

        elif 'delete-workout' in request.POST:
            print(f"Request to delete workout")
            workout.delete()
            return redirect('tracker-home')
        
        elif 'add-set' in request.POST:
            print(f"Request to add set")
            print(request.POST)
            exercise_id = request.POST['add-set']
            print(exercise_id)
            workout_exercise = models.WorkoutExercise.objects.get(id=exercise_id)
            workout_sets = models.Set.objects.filter(workout_exercise=workout_exercise)
            number_of_sets = f"{len(workout_sets) + 1}"
            set = models.Set(workout=workout, workout_exercise=workout_exercise, name=number_of_sets)
            set.save()
            return redirect(workout)
        
        elif 'update-set' in request.POST:
            print(f"Request to update set")
            print(formset.data)
            print(f"Set Form Valid: ", formset.is_valid())
            print(f"Set Form Errors: ", formset.errors)
            if formset.is_valid():
                exercise_id = request.POST['workout_exercise']
                set = formset.save(commit=False)
                set.workout = workout
                set.exercise = models.WorkoutExercise.objects.get(id=exercise_id)
                set.save()

            return redirect(workout)

    return render(request, 'trackerapp/workout-detail.html', context)

def WorkoutExerciseDetail(request, **kwargs):
    id = kwargs.get('id')
    exercise = get_object_or_404(models.WorkoutExercise, id=id)
    workout = models.Workout.objects.get(id=exercise.workout.id)
    sets = models.Set.objects.filter(workout_exercise=exercise)
    number_of_sets = f"Set {len(sets) + 1}"
    form = forms.SetForm(request.POST or None)
    #formset = forms.SetFormset(request.POST or None, initial=[{'name': number_of_sets}])
    formset = forms.SetFormset(request.POST or None, instance=exercise, initial=[{'name': number_of_sets, 'workout': models.Workout.objects.get(id=exercise.workout.id)}])

    if request.method == "POST":
        if 'update-set' in request.POST:
            print(formset.data)
            print(f"Set Form Valid: ", formset.is_valid())
            print(f"Set Form Errors: ", formset.errors)
            if formset.is_valid():
                formset.workout = workout
                formset.save()

            return redirect(exercise)
            
        elif 'add-set' in request.POST:
            set = models.Set()
            set.workout = workout
            set.workout_exercise = exercise
            set.name = number_of_sets
            set.save()

            return redirect(exercise)

    context = {
        'id': id,
        'exercise': exercise,
        'sets': sets,
        'form': form,
        'formset': formset,
    }

    return render(request, 'trackerapp/workout-exercise-detail.html', context)