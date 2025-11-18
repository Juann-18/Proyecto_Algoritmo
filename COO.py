# -------------------------------------------
# Representación de Matrices Dispersas - Formato Coordenado
# -------------------------------------------

def generar_coo(matriz):
    """
    Genera la representación en formato coordenado (COO)
    a partir de una matriz completa.

    Retorna tres listas:
        - valores: lista con los elementos diferentes de cero
        - filas: índice de la fila de cada valor
        - columnas: índice de la columna de cada valor
    """
    valores = []
    filas = []
    columnas = []

    # Recorremos toda la matriz fila por fila
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != 0:     # Solo almacenamos valores no cero
                valores.append(matriz[i][j])
                filas.append(i)
                columnas.append(j)

    return valores, filas, columnas


def imprimir_coo(valores, filas, columnas):
    """
    Imprime la representación COO de forma ordenada.
    """
    print("Representación en Formato Coordenado (COO):\n")
    print("valores  =", valores)
    print("filas    =", filas)
    print("columnas =", columnas)


matriz_ejemplo = [
    [0, 2, 0, 0, 0, 0, 4],
    [0, 8, 9, 0, 0, 1, 0],
    [0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 6, 0],
    [1, 2, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 11, 0]
]

# Obtener formato COO
val, fil, col = generar_coo(matriz_ejemplo)

# Mostrar resultado
imprimir_coo(val, fil, col)

