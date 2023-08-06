3ra entrega de CoderHouse - Python - Comisión 43865

En esta entrega podemos ver la aplicacion de Coder Cafe. En la pagina principal se encuentra un banner de Coder Cafe, los tipos de cafes que venden, información sobre la empresa, sus dueños, formulario de contacto, ubicacion.
En la esquina superior derecha tiene los distintos botones que nos llevará a las distintas vistas de la aplicacion. 

La aplicacion tiene las siguientes clases: cafe, sucursal, cliente, producto, pedido.

Clickeando en CAFE (miaplicacion/cafe) nos lleva a una sección donde podemos ver los distintos tipos de café. 
Luego si presionamos en comprar nos redirecciona para crear un pedido (miaplicacion/crear_pedido/), aqui nos pide los distintos datos del cliente.
El codigo verifica si los datos ingresados coinciden con los de la base de clientes, si no coincide procede a agregarlos a la base. Ademas tambien se agrega el pedido a la base de pedidos.

Volviendo al home, si presionamos en SUCURSALES o en la lupa, nos direcciona al buscador de sucursales (miaplicacion/buscar_sucursales/) donde tenemos un campo para escribir el nombre y nos mostrará las coincidencias.
En esta direccion podemos ver que se hereda el html del home (index.html).
