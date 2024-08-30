productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

listaProductos = productos.split(',')

for producto in listaProductos:
    print(producto.strip())