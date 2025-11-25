# blog/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import registro, LoginCustomView
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

    #path("post/list", views.post_list, name="post_list"),
    path("post/list", views.PostListView.as_view(), name="post_list"),
    #path("post/detail/<int:post_id>/", views.PostDetailView.as_view(), name="post_detail"), 
    path("post/create/", views.PostCreateView.as_view(), name="post_form"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/detail/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
    #path("perfil/", views.perfil, name="perfil"),
    path("editar_perfil/", views.editar_perfil, name="editar_perfil"),

    path('login/', LoginCustomView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', LogoutView.as_view(next_page='blog:index'), name='logout'),
    path('registro/', registro, name='registro'),
    path('accounts/profile/', views.perfil, name='perfil'),


    #path("post/create/", views.post_create, name="post_form"),
    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    #path("post/<int:post_id>/", views.post_detail, name="post_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
