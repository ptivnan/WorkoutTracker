from django import forms
from django.forms import widgets
from . import models

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = models.Workout
        fields = '__all__'
        widgets = {
            'complete': forms.CheckboxInput(
                attrs= {
                    'class': 'btn-check',
                    'id': 'complete'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Give your workout a name...",
                    'class': 'form-control text-center'
                }
            ),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control'
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
        fields = '__all__'
        widgets = {
            'workout': forms.HiddenInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['exercise'].widget.attrs.update({'class': 'form-control', 'onchange': 'this.form.submit()'})
        self.fields['exercise'].empty_label = "Add an exercise..."

class WorkoutExerciseListForm(forms.Form):
    exercise_list = forms.ModelMultipleChoiceField(
        queryset=models.WorkoutExercise.objects.all().order_by('exercise'),
        widget=forms.SelectMultiple(
            attrs={
                'id': 'workout_exercise_list',
            }
        )
    )

SetFormset = forms.inlineformset_factory(models.WorkoutExercise, models.Set, fields=('__all__'), extra=0, can_delete=True)
WorkoutFormset = forms.inlineformset_factory(
    models.Workout, 
    models.Set, 
    fields=('__all__'), 
    extra=0, 
    can_delete=True,
    widgets = {
        'weight': forms.NumberInput(
            attrs = {
                'class': 'form-control text-center',
            }
        ),
        'reps': forms.NumberInput(
            attrs = {
                'class': 'form-control text-center',
            }
        ),
        'failure': forms.CheckboxInput(
            attrs = {
                'class': 'btn-check',
            }
        ),
        'name': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'hidden': 'true',
            }
        ),
        'id': forms.HiddenInput(
            attrs={
                'class': 'form-control'
            }
        ),
        'workout_exercise': forms.HiddenInput(
            attrs={
            'class': 'form-control'
            }
        )
    }
    )
