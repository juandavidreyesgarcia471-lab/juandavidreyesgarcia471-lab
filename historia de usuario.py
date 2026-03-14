# Programa simple para registrar un producto en el inventario

# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar y validar el precio
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: ingrese un valor numérico para el precio.")

# Solicitar y validar la cantidad
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: ingrese un número entero para la cantidad.")

# Calcular el costo total
costo_total = precio * cantidad

# Mostrar resultados
print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", costo_total)

# El programa pide el nombre, precio y cantidad de un producto,
# valida los datos numéricos y calcula el costo total.
