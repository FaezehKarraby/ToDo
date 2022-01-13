from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import AccountForm
User = get_user_model()


class SignUp(CreateView):
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'