from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    #fecha_publicacion = models.DateField(auto_now_add=False, auto_now=False)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.BORRADOR)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.titulo

 
class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.post.titulo}"


