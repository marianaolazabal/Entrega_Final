from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy 
from .models import Post
from .forms import PostForm, EditUserForm
from django.contrib.auth.decorators import login_required
from .forms import EditUserForm, AvatarForm
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView




def about(request):
    return render(request,'blog/about.html')


def perfil(request):
    return render(request,'blog/perfil.html')


from django.contrib.auth import authenticate, login
from .forms import RegistroForm






#class LoginCustomView(LoginView):
#    template_name = "blog/login.html"


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form=EditUserForm(request.POST, instance=request.user)
        #Verificar si el usuario tiene un avatar
        try: 
            avatar=request.user.avatar
        except Avatar.DoesNotExist:
            avatar=None
        
        #Crear el formulario de avatar segun si el usuario tiene uno o no
        if avatar:
            avatar_form=AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form=AvatarForm(request.POST, request.FILES)
        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance=avatar_form.save(commit=False)
            avatar_instance.user=request.user
            avatar_instance.save()
            return redirect('blog:perfil')
    else:
        form = EditUserForm(instance=request.user)
        if hasattr(request.user, 'avatar'):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(request, 'blog/editar_perfil.html', {'form': form, 'avatar_form': avatar_form})

        #if form.is_valid():
        #    form.save()
        #    return redirect('blog:perfil')
    #else:
    #    form=EditUserForm(instance=request.user)
    #return render(request, 'blog/editar_perfil.html', {'form': form})


def index(request):
    return render(request,'blog/index.html')


def post_list(request):
    busqueda=request.GET.get("busqueda", None)
    if busqueda:
        post_list=Post.objects.filter(titulo__icontains=busqueda)
    else:
        post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', context={"posts": post_list})


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        QuerySet = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda:
            QuerySet = QuerySet.filter(titulo__icontains=busqueda)
        return QuerySet




##def post_detail(request, post_id):
#    post = get_object_or_404(Post, id=post_id)
#    return render(request, 'blog/post_detail.html', {"post": post})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect("blog:post_list")
            else:
                form.add_error(None, "Debes estar autenticado para crear una publicación.")
    else:
        form = PostForm()  # ← se define acá también

    return render(request, "blog/post_form.html", {"form": form})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes estar autenticado para crear una publicación.")
            return self.form_invalid(form)
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_edit.html", {"form": form, "post": post})




#def borrar_estudiante(request, estudiante_id):
#    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
#    if request.method == "POST":
#        estudiante.delete()
#        return redirect("lista_de_estudiantes")
    
#    return render(request, "blog/borrar_estudiante.html", {"estudiante": estudiante})


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    #template_name = 'blog/post_confirm_delete.html'

