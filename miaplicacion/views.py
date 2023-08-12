from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.template import Context
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def index(request):
    context = {'current_page': 'inicio'}
    return render(request, "miaplicacion/index.html", context)

def blog(request):
    return render(request, "miaplicacion/blog.html")

def cafe(request):
    cafes = Cafe.objects.all()
    return render(request, "miaplicacion/cafe.html", {'cafes': cafes})

def contacto(request):
    return render(request, "miaplicacion/contacto.html")

def about(request):
    return render(request, "miaplicacion/about.html")


def crear_cafe(request):
    if request.method == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe')  
    else:
        form = CafeForm()
    
    return render(request, 'miaplicacion/crear_cafe.html', {'form': form})

def crear_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sucursales')  
    else:
        form = SucursalForm()
    
    return render(request, 'miaplicacion/crear_sucursal.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  
    else:
        form = SucursalForm()
    
    return render(request, 'miaplicacion/crear_cliente.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')  
    else:
        form = ProductoForm()
    
    return render(request, 'miaplicacion/crear_producto.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            cliente_nombre = form.cleaned_data['cliente_nombre']
            cliente_direccion = form.cleaned_data['cliente_direccion']
            cliente_zona = form.cleaned_data['cliente_zona']
            cliente_telefono = form.cleaned_data['cliente_telefono']
            
            cliente, created = Cliente.objects.get_or_create(
                nombre=cliente_nombre,
                defaults={'direccion': cliente_direccion, 'zona': cliente_zona, 'telefono': cliente_telefono}
            )

            pedido = form.save(commit=False)
            pedido.cliente = cliente
            pedido.save()
            form.save_m2m()

            messages.success(request, 'El pedido se creó con éxito.')

            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    
    return render(request, 'miaplicacion/crear_pedido.html', {'form': form})


def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'miaplicacion/lista_sucursales.html', {'sucursales': sucursales})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'miaplicacion/lista_pedidos.html', {'pedidos': pedidos})


def buscar_sucursales(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            sucursales = Sucursal.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(direccion__icontains=busqueda) |
                Q(zona__icontains=busqueda) |
                Q(telefono__icontains=busqueda) |
                Q(horario_atencion__icontains=busqueda)
            )
        else:
            sucursales = Sucursal.objects.all()
    else:
        form = BusquedaForm()
        sucursales = Sucursal.objects.all()

    context = {'current_page': 'buscar_sucursales'}
    return render(request, 'miaplicacion/buscar_sucursales.html', {'form': form, 'sucursales': sucursales})