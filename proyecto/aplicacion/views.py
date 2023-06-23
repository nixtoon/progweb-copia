from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import CategoriaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    obras = Obra.objects.all()
    artistas = Artista.objects.all()
    data = {
        'obras' : obras,
        'artistas' : artistas
    }
    return render(request, 'app/index.html', data)

def contacto(request):
    context = {}
    return render(request, 'app/plantillas/contacto.html')

def iniciar(request):
    context = {}
    return render(request, 'app/plantillas/iniciar.html')

def iniciar_artista(request):
    context = {}
    return render(request, 'app/plantillas/iniciar_artista.html')

def registrarse(request):
    context = {}
    return render(request, 'app/plantillas/registrarse.html')

def checkout(request):
    context = {}
    return render(request, 'app/plantillas/checkout.html')

# views de las categorias

def  pinturas(request):
    pinturas = Obra.objects.raw('SELECT * FROM aplicacion_obra WHERE categoria_id = 1')
    data = {
        'pinturas': pinturas
    }
    return render(request, 'app/plantillas/categorias/pinturas.html', data)

def escultura(request):
    escultura = Obra.objects.raw('SELECT * FROM aplicacion_obra WHERE categoria_id = 4')
    data = {
        'escultura': escultura
    }
    return render(request, 'app/plantillas/categorias/escultura.html', data)

def orfebreria(request):
    orfebreria = Obra.objects.raw('SELECT * FROM aplicacion_obra WHERE categoria_id = 2')
    data = {
        'orfebreria': orfebreria
    }
    return render(request, 'app/plantillas/categorias/orfebreria.html', data)

def tejidos(request):
    tejidos = Obra.objects.raw('SELECT * FROM aplicacion_obra WHERE categoria_id = 3')
    data = {
        'tejidos': tejidos
    }
    return render(request, 'app/plantillas/categorias/tejidos.html', data)


# views de los artistas

def constanza(request):
    obras = Obra.objects.raw("SELECT * FROM aplicacion_obra WHERE artista_id = '33333333-3'")
    artista = Artista.objects.raw("SELECT * FROM aplicacion_artista WHERE rut = '33333333-3'")
    data = {
        'obras': obras,
        'artista': artista,
    }
    return render(request, 'app/plantillas/artistas/constanza.html', data)

def genesis(request):
    obras = Obra.objects.raw("SELECT * FROM aplicacion_obra WHERE artista_id = '44444444-4'")
    artista = Artista.objects.get(rut = '44444444-4')
    data = {
        'obras': obras,
        'artista': artista,
    }
    return render(request, 'app/plantillas/artistas/genesis.html', data)

def jose(request):
    obras = Obra.objects.raw("SELECT * FROM aplicacion_obra WHERE artista_id = '22222222-2'")
    artista = Artista.objects.get(rut = '22222222-2')
    data = {
        'obras': obras,
        'artista': artista,
    }
    return render(request, 'app/plantillas/artistas/jose.html', data)

def mari(request):
    obras = Obra.objects.raw("SELECT * FROM aplicacion_obra WHERE artista_id = '11111111-1'")
    artista = Artista.objects.get(rut = '11111111-1')
    data = {
        'obras': obras,
        'artista': artista,
    }
    return render(request, 'app/plantillas/artistas/mari.html', data)


# views de las obras

def detalle_producto(request, id):
    obra = get_object_or_404(Obra, id=id)
    data = {
        'obra': obra,
    }
    return render(request, 'app/plantillas/detalle_producto.html', data)

# crud obras con formulario normal

def agregar_obras(request):
    categorias = Categoria.objects.all()
    artistas   = Artista.objects.all()

    data = {
        'categorias': categorias,
        'artistas'  : artistas
    }

    if request.method == 'POST':

        titulo           = request.POST["titulo"]
        categoria        = request.POST["categoria"]
        artista          = request.POST["artista"]
        precio           = request.POST["precio"]
        fechaPublicacion = request.POST["fecha"]
        descripcion      = request.POST["descripcion"]

        objCategoria = Categoria.objects.get(id = categoria)
        objArtista   = Artista.objects.get(rut = artista)

        obra = Obra.objects.create(
            titulo            = titulo,
            precio            = precio,
            descripcion       = descripcion,
            fecha_publicacion = fechaPublicacion,
            categoria         = objCategoria,
            artista           = objArtista,
        )
  
        if 'imagen' in request.FILES:
            imagen      = request.FILES['imagen']
            obra.imagen = imagen
            obra.save()
            messages.success(request, 'Obra registrada correctamente')
        else:
            messages.warning(request, 'No se ha seleccionado ninguna imagen')

        return redirect(to='listar_obras')

    return render(request, 'app/plantillas/crud_obras/agregar.html', data)

def listar_obras(request):
    obras = Obra.objects.all()

    data = {
        'obras': obras
    }

    return render(request, 'app/plantillas/crud_obras/listar.html', data)


def modificar_obras(request, id):
    obra       = get_object_or_404(Obra, id= id)
    categorias = Categoria.objects.all()
    artistas   = Artista.objects.all()

    if request.method == 'POST':
        titulo            = request.POST['titulo']
        categoria         = request.POST['categoria']
        artista           = request.POST['artista']
        precio            = request.POST['precio']
        fecha_publicacion = request.POST['fecha']
        descripcion       = request.POST['descripcion']
        
        objCategoria = Categoria.objects.get(id = categoria)
        objArtista   = Artista.objects.get(rut = artista)

        obra.titulo            = titulo
        obra.categoria         = objCategoria
        obra.artista           = objArtista
        obra.precio            = precio
        obra.fecha_publicacion = fecha_publicacion
        obra.descripcion       = descripcion
        
        if 'imagen' in request.FILES:
            imagen      = request.FILES['imagen']
            obra.imagen = imagen
        
        obra.save()
        messages.success(request, 'Obra modificada correctamente')
        return redirect('listar_obras')
    
    data = {
        'obra'      : obra,
        'categorias': categorias,
        'artistas'  : artistas,
    }
    return render(request, 'app/plantillas/crud_obras/modificar.html', data)

def eliminar_obras(request, id):

    try:
        obra = get_object_or_404(Obra, id= id)
        obra.delete()
        messages.success(request, "Eliminado Correctamente")
        obras = Obra.objects.all()

        data = {
            'obras': obras,
        }

        return render(request, 'app/plantillas/crud_obras/listar.html', data)
    
    except:
        messages.warning(request, "Error al eliminar")

        obras = Obra.objects.all()

        data = {
            'obras': obras,
        }

        return render(request, 'app/plantillas/crud_obras/listar.html', data)
    

# crud categorias con django forms 


def listar_categorias(request):
    categorias = Categoria.objects.all()
    data = {
        'categorias':categorias
    }
    return render(request, 'app/plantillas/crud_django_form/listar.html', data)

def modificar_categorias(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    data = {
        'form' : CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoría Modificada Correctamente')
            return redirect(to='listar_categorias')
        else:
            data['form'] = formulario
    return render(request, 'app/plantillas/crud_django_form/modificar.html', data)

def agregar_categorias(request):
    form = CategoriaForm()
    data = {
        'form': form,
    }
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoriaForm()
            messages.success(request, 'Categoría Agregada Correctamente')
            return redirect(to='listar_categorias')
        else:
            data['form'] = form
    return render(request, 'app/plantillas/crud_django_form/agregar.html', data)

def eliminar_categorias(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, 'Categoría Eliminada Correctamente')
    return redirect(to='listar_categorias')