"""
1. Pedir si es ingreso o gasto o salir
2. Si es ingreso
    2.1 Pedir concepto
    2.2 Pedir fecha
    2.3 Pedir cantidad
3. Si es gastos
    3.1 Pedir concepto
    3.2 Pedir fecha
    3.3 Pedir cantidad
    3.4 Pedir categoria
3.5 Si es salir salimos a 7
4. Instancir el movimiento (ingreso o gasto)
5. Almacenar el movimiento en una lista
6. volver a 1

7. Procesar la lista de movimientos para obtener total de ingresos, gastos y saldo final
"""
from kakebo import *; categoria_gastos
from datetime import date

lista_ingresos = []
lista_gastos = []

def validarFecha(fecha):
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False
def es_float_positivo(valor):
    try:
        valor = float(valor)
        if valor >0:
            return True
    except ValueError:
        return False
def es_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False
def es_categoria_valida(cadena):
    if es_entero(cadena):
        entero = int(cadena)
        return es_entero(cadena) and int(cadena) in[categoria.value for categoria in categoria_gastos]
    else:
        return False
def input_concepto():
    concepto = input("Concepto: ")
    while len(concepto) < 5:
        print("El concepto debe tener al menos 5 caracteres")
        concepto = input("Concepto: ")
    return concepto
def input_fecha():
    fecha = input("Fecha (YYYY-MM-DD): ") 
    while not validarFecha(fecha):
        print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
        fecha = input("Fecha (YYYY-MM-DD): ")
    fecha = date.fromisoformat (fecha)  
    return fecha
def input_cantidad():
    cantidad = input("Cantidad: ")
    while not es_float_positivo(cantidad):
        print("introduce un número positivo")
        cantidad = input("Cantidad: ")
    cantidad = float(cantidad)
    return cantidad
def input_categoria():
    print ("Lista de categoria de gastos: ")
    for categoria in categoria_gastos:
        print(f"{categoria.value} - {categoria.name}")
    cat = input("Elige una de las categorias a continuación: ")
    while not es_categoria_valida(cat):
        print("La categoria no es correcta: ")
        print ("Lista de categoria de gastos: ")
        for categoria in categoria_gastos:
            print(f"{categoria.value} - {categoria.name}")
        cat = input("Elige una de las categorias a continuación: ")
    cat= categoria_gastos(int(cat))
    return cat
def obtener_total(lista):
    total = 0
    for movimiento in lista:
        total += movimiento.cantidad
    return total
    


continuar = True
while continuar == True:
    tipo = input("Ingreso, Gasto o Salir (I/G/S): ").lower()

    while tipo not in ('i', 'g', 's'):
        print("Teclea I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()

    if tipo == 'i':
        concepto = input_concepto()
        fecha = input_fecha()
        cantidad = input_cantidad()

        lista_ingresos.append(Ingreso(concepto, fecha, cantidad))

    elif tipo == "g":
        concepto = input_concepto()
        fecha = input_fecha()
        cantidad = input_cantidad()
        categoria = input_categoria()

        lista_gastos.append(  Gasto(concepto, fecha, cantidad, categoria))

    elif tipo == "s":
        continuar = False

total_ingresos = obtener_total(lista_ingresos)
total_gastos = obtener_total(lista_gastos)
saldo = total_ingresos - total_gastos

print (f"El total de los ingresos asciende a: {total_ingresos:10.2f} €")
print (f"El total de gastos asciende a:       {total_gastos:10.2f} €")
print (f"El saldo total asciende a:           {saldo:10.2f} €")