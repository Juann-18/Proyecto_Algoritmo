def matriz_a_csr(matriz):
    valores = []
    columnas = []
    cfilas = [0]
    contador = 0
    for fila in matriz:
        for j, val in enumerate(fila):
            if val != 0:
                valores.append(val)
                columnas.append(j)
                contador += 1
        cfilas.append(contador)
    return valores, columnas, cfilas

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

valores, columnas, cfilas = matriz_a_csr(matriz)
print("valores:", valores)
print("columnas:", columnas)
print("cfilas:", cfilas)
