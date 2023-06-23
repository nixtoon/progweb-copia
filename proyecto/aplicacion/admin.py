from django.contrib import admin
from . models import Obra, Artista, Categoria

# Register your models here.
admin.site.register(Obra)
admin.site.register(Categoria)
admin.site.register(Artista)