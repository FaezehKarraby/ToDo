from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from todo.models import TodoModel

User = get_user_model()


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
