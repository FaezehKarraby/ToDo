from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from todo.forms import TodoForm
from todo.models import TodoModel


def todo_list(request):
    item_list = TodoModel.objects.order_by("date_created")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ToDo:todo_list')
    form = TodoForm()
    context = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST',
    }
    return render(request, 'todo/todo_list.html', context)


def todo_details(request, pk):
    item = get_object_or_404(TodoModel, pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'todo/todo_details.html', context)


def remove(request, pk):
    item = TodoModel.objects.get(pk=pk)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('ToDo:todo_list')
