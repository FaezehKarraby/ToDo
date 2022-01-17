from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import AccountForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()


class SignUp(CreateView):
    form_class = AccountForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


