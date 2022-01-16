from django.urls import path

from account import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

]