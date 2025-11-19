from CSC import matriz_a_csc
from CSR import matriz_a_csr
from COO import matriz_a_coo



def menu(): 
    matriz = []
    if not matriz: 
        matriz = agregar_matriz()
        mostrar_matriz(matriz)
    while(True):
        print("")
        print("Menu Principal")
        print("1. Obtener la representacion")

        opcion = int(input("Ingrese la opcion: "))
        
        if(opcion == 1 ): 
            submenu(matriz)




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
        print("Valores ", val)
        print("filas ", fil)
        print("columnas ", col)
    elif(n == 2):
        val, filas, ccolumnas = matriz_a_csr(matriz)
        print("Valores ", val)
        print("filas ",filas)
        print("ccolumnas ", ccolumnas)


menu()