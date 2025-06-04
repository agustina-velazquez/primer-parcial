
#las filas seran las areas y las columnas los vendedores

#opcion 1: Obtener ventas: para ello deberá generar una función que cargue secuencialmente, de
#tal forma que la intersección de cada fila y cada columna corresponde al valor total de
#ventas en pesos de un vendedor en una zona. Esto es carga secuencial.

def mostrar_matriz(matriz: list)->None:
    '''Recibe una matriz como parámetro y la muestr por consola. No retorna nada.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")

        print(" ")

#cargo ventas y nombres con la misma funcion 
def carga_secuencial(matriz: list, mensaje: str, tipo: str)-> list: 
    '''Recibe una matriz como parámetro, un mensaje y un tipo de elemento. 
    Carga la matriz secuencialmente y la retorna.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(mensaje)
            elemento = input(f"Elemento en fila {i}, columna {j}: ")
            if tipo == "int":
                valor = int(elemento)
                matriz[i][j] = valor
            else:
                matriz[i][j] = elemento
                
    return matriz

#opcion 3: Mostrar nombres de vendedores que hayan vendido más de $500.000. no hay que sumar

def buscar_ventas(matriz_1: list, matriz_2:list, max:int)->list: #los parametros van a ser la matriz de ventas y la matriz de nombre y se supone que me va a devolver una list con los nombres
    '''Recibe dos matrices como parámetros y un valor maximo. Busca en la primera matriz los elementos mayores
    al valor maximo, y agrega a la lista retorno los elementos de la segunda matriz que esten en la mism posicion
    en donde se encontraron los valores maximos
    '''
    vendedores_max = []

    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            if (matriz_1[i][j])>max:
                vendedores_max += [matriz_2[i][j]] 
    
    return vendedores_max

#opcion 4: Mostrar zonas en que se vendieron más de $2.000.000. Voy a tener que sumar por filas y mostrar el elemento de la lista áreas

def sumar_filas_columnas(matriz:list, lugar:str)->list:
    '''Recibe una matriz y un lugar como parámetros y retorna una lista con la suma de cda fila o cada columna
    '''
    lista_suma = []
    suma = 0

    if lugar == "Fila":
        for i in range(len(matriz)):
            suma = 0 
            for j in range(len(matriz[i])):
                suma += matriz[i][j]
            lista_suma += [suma]

    else:
        columnas = len(matriz[0]) 
        for i in range(columnas): #5 iter
            suma = 0
            for j in range(len(matriz)): #4 iter
                suma += matriz[j][i] 
            lista_suma += [suma]

    return lista_suma

def buscar_zonas(lista_1:list, lista_2: list,max:int)->list:
    '''Recibe dos listas como parámetros y un valor maximo. Busca los elementos maximos al valor en la primera lista
    y retorna los elementos de la segunda lista que se encuentran en el mismo indice en donde se encontraron los
    vlores maximos
    '''

    zonas = []

    for i in range(len(lista_1)):
        if lista_1[i]>max:
            zonas += [lista_2[i]]
    
    return zonas


#opcion 5: Obtener el mejor vendedor de cada zona. 

def buscar_maximo(lista:list)->int: #que me retorne el indice en el que se encuentra el maximo
    maximo = 0
    indice = 0
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            indice = i

    return indice

def obtener_maximos(matriz_1: list, matriz_2: list) -> list:
    lista_retorno = []
    for i in range(len(matriz_1)):
        indice_columna = buscar_maximo(matriz_1[i])
        lista_retorno += [matriz_2[i][indice_columna]]
    
    return lista_retorno

#no pude terminarlo. 
#Ya lo termine.

#opcion 6: Cambiar vendedores: se deberá poder cambiar nombres de los vendedores, en la segunda matriz.

def carga_distribuida(matriz:list)->list: 
    '''Recibe una matriz y la carga distrivutivamente o aleatoreamente. Retorna la matriz cargada.
    '''
    
    seguir = "Si"

    while seguir == "Si":
        fila = int(input("Ingrese indicie fila: "))
        columna = int(input("Ingrese indice columna: "))
        valor = input("Ingrese el nuevo nombre: ")
        matriz[fila][columna] = valor
        seguir = input("¿Desea seguir realizando cambios?Si/No: ")
    
    return matriz

#opcion 7: Informe de ingresos de la empresa: tomando en cuenta que existen distintas
#comisiones para los vendedores según la zona se deberá poder estimar los ingresos
#netos de la empresa en cada zona. En zona norte el 30% de las ventas corresponde a
#la comisión del vendedor, en zona sur el 25%, en zona oeste el 20% y en caba el 15%.

def calcular_ingresos_netos(matriz: list, comisiones: list)->list:
    matriz_retorno = matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_retorno[i][j] = matriz[i][j] - (comisiones[i]*matriz[i][j]/100)
    
    return matriz_retorno




    




#opcion 8: Mostrar ventas en otras monedas: se debe poder transformar la matriz en pesos a 
#otras monedas. Para ello se deberá desarrollar una función que reciba por parámetro
#la matriz en pesos, el nombre de una moneda y su cotización. Esta función debe
#poseer parámetros opcionales para transformar el valor a dólares con una cotización
#de 1200.

def cambiar_moneda(matriz:list, moneda:str = "dolar", cotizacion: int = 1200 )->list: 
    '''Recibe unaa matriz como parametro. Una moneda y una cotizacion como opcionales. Retorna la matriz multiplicada 
    por la cotizacion dada
    '''
    matriz_resultdo = matriz
   
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultdo[i][j] = matriz[i][j]/cotizacion
    
    return matriz_resultdo



