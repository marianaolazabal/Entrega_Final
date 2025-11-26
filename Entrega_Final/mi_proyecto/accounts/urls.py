from django.urls import path
from .views import LoginCustomView, registro
from django.urls import path, reverse_lazy

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('login/', LoginCustomView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='blog:index'), name='logout'),
    path('registro/', registro, name='registro'),

    path(
    'password_change/',
    auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url=reverse_lazy('accounts:password_change_done')
    ),
    name='password_change'
    ),

    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'
        ),
        name='password_change_done'
    ),
]
