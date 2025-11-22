from CSC import matriz_a_csc
from CSR import matriz_a_csr
from COO import matriz_a_coo
from Operaciones import obtener_elemento_csr, obtener_elemento_coo, obtener_elemento_csc



def menu(): 
    matriz = []
    if not matriz: 
        matriz = agregar_matriz()
        mostrar_matriz(matriz)
    while(True):
        print("")
        print("Menu Principal")
        print("1. Obtener la representacion")
        print("2. Operaciones")

        opcion = int(input("Ingrese la opcion: "))
        
        if(opcion == 1 ): 
            submenu(matriz)
        if(opcion == 2 ):
            submenu_operaciones(matriz)

def agregar_lista(texto):
    lista = []
    tamaño = int(input("Ingrese el tamaño del vector: "))
    print(texto)
    for i in range(tamaño):
        n = int(input(f"Ingrese el valor para la posición {i+1}: "))
        lista.append(n)
    return lista


def agregar_matriz():
    matriz = [] 
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("ingrese el numero de columnas: "))
    for i in range(filas):
        fila= []
        for j in range(columnas):
            n = int(input("Ingrese un valor: "))
            fila.append(n)
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def submenu(matriz):
    print("1. COO")
    print("2. CSR")
    print("3. CSC")
    n= int(input("Ingrese la opcion: "))
    if(n == 1): 
        val, fil, col = matriz_a_coo(matriz)
        mostrar_matriz(matriz)
        print("")
        print("Valores ", val)
        print("filas ", fil)
        print("columnas ", col)
    elif(n == 2):
        val, columnas, cfilas = matriz_a_csr(matriz)
        mostrar_matriz(matriz)
        print("")
        print("Valores ", val)
        print("columnas ",columnas)
        print("cfilas ", cfilas)
    elif(n == 3):
        val, filas, ccolumnas = matriz_a_csc(matriz)
        mostrar_matriz(matriz)
        print("")
        print("valores ", val)
        print("filas ", filas)
        print("ccolunas ", ccolumnas)

def submenu_operaciones(matriz):
    print("")
    print("1. Obtener elemento")
    n= int(input("Ingrese la opcion: "))
    if(n == 1 ):
        print("")
        print("1. Utilizar la representacion de la matriz principal(CSR)")
        print("2. ingresar la representacion")
        m= int(input("Ingrese la opcion: "))
        if(m == 1):
            i = int(input("ingrese el valor de i: "))
            j = int(input("ingrese el valor de j: "))
            val, columnas, cfilas = matriz_a_csr(matriz)
            mostrar_matriz(matriz)
            print("")
            print(f'El elemto en la posicion {i},{j} es {obtener_elemento_csr(i,j,val,columnas,cfilas)}')

        if(m == 2):
            print("1. COO")
            print("2. CSR")
            print("3. CSC")

            o = int(input("Ingrese la opcion"))
            if (o == 1 ):
                val = agregar_lista("Vector de valores")
                filas = agregar_lista("Vector de filas")
                columnas = agregar_lista("Vector de columnas")

                i = int(input("ingrese el valor de i: "))
                j = int(input("ingrese el valor de j: "))
                print("")
                print(f'El elemto en la posicion {i},{j} es {obtener_elemento_coo(i,j,val,filas,columnas)}')
            elif( o == 2): 
                
                val = agregar_lista("Vector de valores")
                columnas = agregar_lista("Vector de culumnas")
                cfilas = agregar_lista("Vector de cfilas")

                i = int(input("ingrese el valor de i: "))
                j = int(input("ingrese el valor de j: "))
                print("")
                print(f'El elemto en la posicion {i},{j} es {obtener_elemento_csr(i,j,val,columnas,cfilas)}')
            elif( o == 3):
                val = agregar_lista("Vector de valores")
                filas = agregar_lista("Vector de filas")
                ccolumnas = agregar_lista("Vector de ccolumna")

                i = int(input("ingrese el valor de i: "))
                j = int(input("ingrese el valor de j: "))
                print("")
                print(f'El elemto en la posicion {i},{j} es {obtener_elemento_csc(i,j,val,filas,ccolumnas)}')









menu()