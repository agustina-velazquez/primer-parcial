from paquete.ejercicio import *

areas = ["CABA", "zona sur", "zona oeste", "zona norte"] #filas
vendedores = ["vendedor 1", "vendedor 2", "vendedor 3", "vendedor 4", "vendedor 5"] #columnas

matriz_vacia = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

print("Menú de opciones:")
print("Opción 1: Obtener ventas")
print("Opción 2: Obtener vendedores")
print("Opción 3: Mostrar nombres de vendedores que hayan vendido más de $500.000.")
print("Opción 4: Mostrar zonas en que se vendieron más de $2.000.000.")
print("Opción 5: Obtener el mejor vendedor de cada zona.")
print("Opción 6: Cambiar vendedores.")
print("opcion 8: Mostrar ventas en otra moneda.")


menu = True

while menu == True:
    opcion = int(input("Bienvenido/a. Ingrese su opcion: "))

    match opcion:
        case 1:
            print("Opción 1: Obtener ventas")
            print("Comienza la carga de ventas: ")
            matriz_ventas = carga_secuencial(matriz_vacia)
            print("La matriz con las ventas es la siguiente")
            mostrar_matriz(matriz_ventas)
        case 2:
            print("Opción 2: Obtener vendedores")
            print("Comienza la carga de los nombres de los vendedores: ")
            matriz_vendedores = carga_secuencial(matriz_vacia)
            print("Matriz con los nombres de los vendedores: ")
            mostrar_matriz(matriz_vendedores)
        case 3:
            print("Opción 3: Mostrar nombres de vendedores que hayan vendido más de $500.000.")
            vendedores = buscar_ventas(matriz_ventas,matriz_vendedores,500000)
            print(f"Los vendedores que vendieron mas de $500.000 son: {vendedores}")
        case 4:
            print("Opción 4: Mostrar zonas en que se vendieron más de $2.000.000.")
            suma_zonas = sumar_filas_columnas(matriz_ventas, "Fila")
            zonas = buscar_zonas(suma_zonas, areas,2000000)
            print(f"Las zonas en las que se vendieron mas de $2.000.000 son: {zonas}")
        case 6:
            print("Opcion 6: Cambiar vendedores")
            print("Se realizaran algunos cambios en los vendedores")
            matriz_vendedores_modificada = carga_distribuida(matriz_vendedores)
            print("La matriz de vendedores se modifico, esta es la nueva: ")
            mostrar_matriz(matriz_vendedores_modificada)
        case 8:
            print("Opción 8: Mostrar ventas en otra moneda.")
            matriz_cotizada = cambiar_moneda(matriz_ventas) #cambiando los parametros opcionales tambien funciona
            print("Matriz en la moneda elegida: ")
            mostrar_matriz(matriz_cotizada)
        case 10: 
            menu = False

