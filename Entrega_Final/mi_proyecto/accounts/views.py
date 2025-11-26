from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from blog.forms import RegistroForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView



class LoginCustomView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('blog:index')



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            return redirect('accounts:login')
    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {"form": form})