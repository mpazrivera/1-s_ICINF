# Información de los productos
productos = ["Smartphone", "Laptop", "Tablet", "Smartwatch"]
precios = [300, 800, 150, 200]
stock = {
    "Smartphone": 25,
    "Laptop": 12,
    "Tablet": 8,
    "Smartwatch": 4
}

#Encontrar el producto más caro y más barato
precio_max = max(precios)
precio_min = min(precios)

producto_mas_caro = productos[precios.index(precio_max)]
producto_mas_barato = productos[precios.index(precio_min)]

print("Producto más caro:", producto_mas_caro, "- $", precio_max, "")
print("Producto más barato:", producto_mas_barato, "- $", precio_min, "")
print()

#Clasificar productos por categoría de precio
print("Categoría de precio por producto:")
for i in range(len(productos)):
    producto = productos[i]
    precio = precios[i]
    
    if precio < 200:
        categoria = "Producto Económico"
    elif 200 <= precio <= 500:
        categoria = "Producto Estándar"
    else:
        categoria = "Producto Premium"
    
    print(f"{producto}: {categoria}")
print()

#Listar productos con stock bajo (<10 unidades)
print("Productos con stock bajo:")
for producto in productos:
    if stock[producto] < 10:
        print(f"{producto} -> {stock[producto]} unidades")
