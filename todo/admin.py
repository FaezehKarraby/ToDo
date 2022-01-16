from django.contrib import admin

from todo.models import TodoModel


class TodoAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject']


admin.site.register(TodoModel, TodoAdmin)
