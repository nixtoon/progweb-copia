from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('iniciar_artista/', views.iniciar_artista, name='iniciar_artista'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('checkout/', views.checkout, name='checkout'),
    path('pinturas/', views.pinturas, name='pinturas'),
    path('escultura/', views.escultura, name='escultura'),
    path('orfebreria/', views.orfebreria, name='orfebreria'),
    path('tejidos/', views.tejidos, name='tejidos'),
    path('constanza/', views.constanza, name='constanza'),
    path('genesis/', views.genesis, name='genesis'),
    path('jose/', views.jose, name='jose'),
    path('mari/', views.mari, name='mari'),
    path('detalle-producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    
    path('listar-obras/', views.listar_obras, name='listar_obras'),
    path('modificar-obras/<id>/', views.modificar_obras, name='modificar_obras'),
    path('agregar-obras/', views.agregar_obras, name='agregar_obras'),
    path('eliminar_obras/<int:id>/', views.eliminar_obras, name='eliminar_obras'),

    path('listar-categorias/', views.listar_categorias, name='listar_categorias'),
    path('modificar-categorias/<id>/', views.modificar_categorias, name='modificar_categorias'),
    path('agregar-categorias/', views.agregar_categorias, name='agregar_categorias'),
    path('eliminar_categorias/<int:id>/', views.eliminar_categorias, name='eliminar_categorias'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]