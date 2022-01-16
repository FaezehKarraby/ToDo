from django.urls import path

from todo import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('del/<int:pk>/', views.remove, name='del'),
]