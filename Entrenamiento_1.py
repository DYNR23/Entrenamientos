def calcular_costo_total():
    # Solicitar los datos al usuario con mensajes claros
    nombre_producto = input("Ingrese el nombre del producto: ")
    
    while True: 
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario < 0 and precio_unitario == (" ","  ", "   "):
                print("El precio no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos adquiridos: "))
            if cantidad < 0 and cantidad == (" ","  ", "   "): 
                print("La cantidad no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero válido para la cantidad.")

    while True:
        try:
            porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (0 si no aplica): "))
            if porcentaje_descuento < 0 or porcentaje_descuento > 100 and porcentaje_descuento == (" ","  ", "   "):
                print("El porcentaje debe estar entre 0 y 100. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para el descuento.")

    # Calcular el costo total sin descuento
    costo_bruto = precio_unitario * cantidad

    # Calcular el valor del descuento
    descuento = (porcentaje_descuento / 100) * costo_bruto

    # Calcular el monto total a pagar
    total_pagar = costo_bruto - descuento

    # Mostrar el resultado de manera clara y con dos decimales
    print("\nResumen de la compra:")
    print(f"Producto: {nombre_producto}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Descuento aplicado: {porcentaje_descuento:.2f}%")
    print(f"Costo total sin descuento: ${costo_bruto:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total_pagar:.2f}")

# Ejecutar el programa
calcular_costo_total()