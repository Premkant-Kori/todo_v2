from django import forms
from .models import TaskTable

class TaskTableForm(forms.ModelForm):
    class Meta:
        model = TaskTable
        fields = ['task_column',]
        widgets = {
            'task': forms.TextInput(attrs={'class':'form-control', 'maxlength':"27"}),
        }
        labels = {
            'task_column': '',
        }