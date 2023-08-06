from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, "miaplicacion/index.html")

def blog(request):
    return render(request, "miaplicacion/blog.html")

def cafe(request):
    return render(request, "miaplicacion/cafe.html")

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
            return redirect('lista_producto')  
    else:
        form = ProductoForm()
    
    return render(request, 'miaplicacion/crear_producto.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
        
            cliente_nombre = form.cleaned_data['cliente_nombre']
            cliente, created = Cliente.objects.get_or_create(nombre=cliente_nombre)
            pedido = form.save(commit=False)
            pedido.cliente = cliente
            pedido.save()

            form.save_m2m()  
            return redirect('lista_pedidos')  
    else:
        form = PedidoForm()
    
    return render(request, 'miaplicacion/crear_pedido.html', {'form': form})


def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'miaplicacion/lista_sucursales.html', {'sucursales': sucursales})


def buscar_sucursales(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            sucursales = Sucursal.objects.filter(nombre__icontains=busqueda)
        else:
            sucursales = Sucursal.objects.all()
    else:
        form = BusquedaForm()
        sucursales = Sucursal.objects.all()

    return render(request, 'miaplicacion/buscar_sucursales.html', {'form': form, 'sucursales': sucursales})