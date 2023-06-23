from django.db import models

# Create your models here.
class Artista(models.Model):
  rut              = models.CharField(primary_key=True, max_length=10)
  nombre           = models.CharField(max_length=20)
  apellido_paterno = models.CharField(max_length=20)
  apellido_materno = models.CharField(max_length=20)
  fecha_nacimiento = models.DateField(blank=False, null=False)
  telefono         = models.CharField(max_length=20)
  email            = models.EmailField(unique=True, max_length=80, blank=True, null=True)
  direccion        = models.CharField(max_length=80, blank=True, null=True)
  activo           = models.BooleanField()  

  def __str__(self):
    return str(self.nombre)+" "+str(self.apellido_paterno)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Obra(models.Model):
    titulo            = models.CharField(max_length=50)
    precio            = models.IntegerField()
    descripcion       = models.TextField()
    fecha_publicacion = models.DateField()
    imagen            = models.ImageField(upload_to="productos", null = True)
    url               = models.CharField(max_length=50, blank=True, null= True)
    categoria         = models.ForeignKey(Categoria, on_delete = models.PROTECT)
    artista           = models.ForeignKey(Artista, on_delete = models.PROTECT)

    def __str__(self):
        return self.titulo