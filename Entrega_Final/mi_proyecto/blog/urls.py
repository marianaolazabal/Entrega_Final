from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

    path("post/list", views.PostListView.as_view(), name="post_list"),
    path("post/create/", views.PostCreateView.as_view(), name="post_form"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/detail/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),

    path("editar_perfil/", views.editar_perfil, name="editar_perfil"),
    path("post/perfil/", views.perfil, name="perfil"),

    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
