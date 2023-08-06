from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio" ),

    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('cafe/', cafe, name="cafe"),
    path('contacto/', contacto, name="contacto"),

    path('crear_cafe/', crear_cafe, name='crear_cafe'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_sucursal/', crear_sucursal, name='crear_sucursal'),

    path('lista_sucursales/', lista_sucursales, name='lista_sucursales'),

    path('buscar_sucursales/', buscar_sucursales, name='buscar_sucursales'),

]