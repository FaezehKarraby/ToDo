from django import forms
from todo.models import TodoModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        exclude = ('user', )

    def save(self, user):
        todo = super().save(commit=False)
        todo.user = user
        todo.save(todo.user)