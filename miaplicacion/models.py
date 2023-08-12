from django.db import models

# Create your models here.

class Cafe(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    aroma = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    zona = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    horario_atencion = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    nro_cuenta_pesos = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=100, default='')  
    zona = models.CharField(max_length=100, default='')  
    telefono = models.CharField(max_length=20, default='')  
    productos = models.ManyToManyField(Producto)
    

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.fecha_pedido}"