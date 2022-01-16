from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from todo.forms import TodoForm
from todo.models import TodoModel


@login_required
def todo_list(request):
    item_list = TodoModel.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('ToDo:todo_list')
    form = TodoForm()
    context = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST',
    }
    return render(request, 'todo/todo_list.html', context)


def remove(request, pk):
    item = TodoModel.objects.get(pk=pk)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('ToDo:todo_list')
