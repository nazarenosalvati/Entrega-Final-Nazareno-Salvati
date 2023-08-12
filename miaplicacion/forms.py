from django import forms
from .models import *

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['nombre', 'region', 'aroma', 'sabor']

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'zona', 'telefono', 'horario_atencion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'nro_cuenta_pesos']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cafe', 'nombre', 'descripcion', 'precio']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente_nombre', 'cliente_direccion', 'cliente_zona', 'cliente_telefono', 'productos']
    cliente_nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del cliente'}))
    cliente_direccion = forms.CharField(label='Direccion', widget=forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del cliente'}))
    cliente_zona = forms.CharField(label='Zona', widget=forms.TextInput(attrs={'placeholder': 'Ingrese la zona del cliente'}))
    cliente_telefono = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono del cliente'}))
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.Select())


class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Buscar', max_length=100)