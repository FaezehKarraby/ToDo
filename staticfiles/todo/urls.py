from django.urls import path

from todo import views

urlpatterns = [
    path('todo/list/', views.todo_list, name='todo_list'),
    path('todo/details/<int:pk>/', views.todo_details, name='todo_details'),
    path('del/<int:pk>/', views.remove, name='del'),
]