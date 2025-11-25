from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Post, Categoria, Comentario
from .models import Avatar


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']


class RegistroForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmar contraseña"
    )

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("password2")
        if p1 != p2:
            self.add_error("password2", "Las contraseñas no coinciden")
        return cleaned_data

       
class EditUserForm(UserChangeForm):
    email=forms.EmailField(required=True, label='Email')
    first_name=forms.CharField(required=True, label='Nombre')
    last_name=forms.CharField(required=True, label='Apellido')

    class Meta:
        model=User
        fields=['email', 'first_name', 'last_name', 'password']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción (opcional)'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'estado', 'contenido', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
            #'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor del post'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe el contenido aquí...'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }
