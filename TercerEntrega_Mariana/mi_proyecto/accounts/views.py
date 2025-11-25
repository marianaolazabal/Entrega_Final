from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class LoginCustomView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy('post_list')
