from paquete.ejercicio import *

areas = ["CABA", "zona sur", "zona oeste", "zona norte"] #filas
vendedores = ["vendedor 1", "vendedor 2", "vendedor 3", "vendedor 4", "vendedor 5"] #columnas

matriz_vacia_1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
matriz_vacia_2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


menu = True
opcion_1 = False
opcion_2 = False

while menu == True:
    print("Menú de opciones: ")
    print("Opción 1: Obtener ventas.")
    print("Opción 2: Obtener vendedores.")
    print("Opción 3: Mostrar nombres de vendedores que hayan vendido mas de $500.000.")
    print("Opción 4: Mostrar zonas en que se vendieron más de $2.000.000.")
    print("Opción 5: Obtener el mejor vendedor de cada zona.")
    print("Opción 6: Cambiar vendedores.")
    print("Opción 7: Informes de ingresos de la empresa.")
    print("Opción 8: Mostrar ventas en otra moneda.")


    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        print("Opción 1: Obtener ventas")
        print("Comienza la carga de ventas: ")
        matriz_ventas = carga_secuencial(matriz_vacia_1, "Ingrese el valor de la venta realizada:", "int")
        print("La matriz con las ventas es la siguiente:")
        mostrar_matriz(matriz_ventas)
        opcion_1 = True
    elif opcion == 2:
        if opcion_1 == True:
            print("Opción 2: Obtener vendedores")
            print("Comienza la carga de los nombres de los vendedores: ")
            matriz_vendedores = carga_secuencial(matriz_vacia_2, "Ingrese el nombre del vendedor: ", "str")
            print("Matriz con los nombres de los vendedores: ")
            mostrar_matriz(matriz_vendedores)
            opcion_2 = True
        else:
            print("Se debe ingresar primero la opción 1 para continuar")
    else:
        if not(opcion_1 and opcion_2):
            print("Se debe ingresar primero la opcion 1, luego la 2 para poder continuar")
        else:
            match opcion:
                case 3:
                    print("Opción 3: Mostrar nombres de vendedores que hayan vendido más de $500.000.")
                    vendedores = buscar_ventas(matriz_ventas, matriz_vendedores, 500000)
                    print(f"Los vendedores que vendieron mas de $500.000 son: {vendedores}")
                case 4:
                    print("Opción 4: Mostrar zonas en que se vendieron más de $2.000.000.")
                    suma_zonas = sumar_filas_columnas(matriz_ventas, "Fila")
                    zonas = buscar_zonas(suma_zonas, areas,2000000)
                    print(f"Las zonas en las que se vendieron mas de $2.000.000 son: {zonas}")
                case 5:
                    print("Opción 5: Obtener el mejor vendedor de cada zona.")
                    mejores_vendedores = obtener_maximos(matriz_ventas, matriz_vendedores)
                    for i in range (len(matriz_ventas)):
                        print(f"En {areas[i]} el mejor vendedor es {mejores_vendedores[i]}")
                case 6:
                    print("Opcion 6: Cambiar vendedores")
                    print("Se realizaran algunos cambios en los vendedores")
                    matriz_vendedores_modificada = carga_distribuida(matriz_vendedores)
                    print("La matriz de vendedores se modifico, esta es la nueva: ")
                    mostrar_matriz(matriz_vendedores_modificada)
                case 7:
                    print("Opción 7: Informes de ingresos de la empresa.")
                    comisiones = [15,25,20,30]
                    matriz_ingresos_netos = calcular_ingresos_netos(matriz_ventas, comisiones)
                    ingresos_netos_zonas = sumar_filas_columnas(matriz_ingresos_netos, "Fila")
                    for i in range(len(matriz_ingresos_netos)):
                        print(f"En {areas[i]} el ingreso neto es de ${ingresos_netos_zonas[i]}")
                case 8:
                    print("Opción 8: Mostrar ventas en otra moneda.")
                    moneda = input("Nombre de la moneda: ")
                    cotizacion = int(input("Cotización de la moneda: "))
                    matriz_cotizada = cambiar_moneda(matriz_ventas, moneda, cotizacion) #cambiando los parametros opcionales tambien funciona
                    print("Matriz en la moneda elegida: ")
                    mostrar_matriz(matriz_cotizada)
                case 10: 
                    menu = False



 