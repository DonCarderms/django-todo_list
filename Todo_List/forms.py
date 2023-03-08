from django import forms

from Todo_List.models import Todo

class newTodo(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        