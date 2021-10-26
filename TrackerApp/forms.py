from django import forms
from . import models

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = models.Workout
        fields = '__all__'
        widgets = {
            'complete': forms.CheckboxInput(
                attrs= {
                    'class': 'btn-check',
                    'id': 'btn-complete'
                }
            )
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = models.Exercise
        fields = '__all__'


class SetForm(forms.ModelForm):
    class Meta:
        model = models.Set
        fields = '__all__'

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = models.WorkoutExercise
        exclude = ['workout']

class WorkoutExerciseListForm(forms.Form):
    exercise_list = forms.ModelMultipleChoiceField(
        queryset=models.WorkoutExercise.objects.all().order_by('exercise'),
        widget=forms.SelectMultiple(
            attrs={
                'id': 'workout_exercise_list',
            }
        )
    )

SetFormset = forms.inlineformset_factory(models.WorkoutExercise, models.Set, fields=('__all__'), extra=0, can_delete=True )