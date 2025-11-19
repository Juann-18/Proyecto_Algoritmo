def matriz_a_csc(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    valores = []
    filas_idx = []
    ccolumnas = [0]
    contador = 0
    for j in range(columnas):
        for i in range(filas):
            if matriz[i][j] != 0:
                valores.append(matriz[i][j])
                filas_idx.append(i)
                contador += 1
        ccolumnas.append(contador)
    return valores, filas_idx, ccolumnas

# Ejemplo de uso:
matriz = [
    [0, 2, 0, 0, 0, 0, 4],
    [0, 8, 9, 0, 0, 1, 0],
    [0, 0, 0, 3, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0],
    [1, 2, 0, 0, 0, 6, 0],
    [4, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 11, 0]
]

# valores, filas_idx, ccolumnas = matriz_a_csc(matriz)
# print("valores:", valores)
# print("filas:", filas_idx)
# print("ccolumnas:", ccolumnas)
