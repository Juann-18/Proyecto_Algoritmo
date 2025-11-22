def obtener_elemento_csr(i,j, valores, posicion, cAcumulativo):

    for k in range(cAcumulativo[i], cAcumulativo[i+1]):
        if (posicion[k] == j):
            return valores[k]
    return 0

def obtener_elemento_csc(i, j, valores, filas, ccolumnas):
    for k in range(ccolumnas[j], ccolumnas[j+1]):
        if filas[k] == i:
            return valores[k]
    return 0


def obtener_elemento_coo(i, j, valores, filas, columnas):

    for k in range(len(valores)):
        if filas[k] == i and columnas[k] == j:
            return valores[k]
    return 0
# print(obtener_elemento(1,1,[ 2,4,8,9,1,3,5,6,1,2,4,7,1,1], [1,6,1,2,5,3,0,5,0,1,0,2,5], [0,2,5,6,6,8,10,11,13]
# ))
