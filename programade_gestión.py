# A. Ingresar el nombre del producto y su precio unitario
nombre_producto = input("Ingresa el nombre del producto: ")
precio_unitario = float(input("Ingresa el precio unitario del producto: "))

# B. Ingresar la cantidad en stock
cantidad_stock = int(input("Ingresa la cantidad en stock: "))

# C. Calcular el valor total de los productos
valor_total = precio_unitario * cantidad_stock

# D. Evaluar el umbral
umbral = valor_total > 100000

# E. Imprimir toda la información formateada
print(f"Producto: {nombre_producto} | Cantidad: {cantidad_stock} | Valor Total: ${valor_total:.2f} | Sobre umbral: {umbral}")