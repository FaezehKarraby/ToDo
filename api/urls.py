from django.urls import path

from api import views

urlpatterns = [
    path('tasks/', views.GetTodoList.as_view(), name='list'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='detail'),

    path('users/', views.UserList.as_view(), name='list_user'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='detail_user'),

    path('get_status/', views.get_todo_by_status, name='todo_by_status'),
]
