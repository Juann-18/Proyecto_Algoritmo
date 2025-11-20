def obtener_elemento(i,j, valores, posicion, cAcumulativo):

    for k in range(cAcumulativo[i], cAcumulativo[i+1]):
        if (posicion[k] == j):
            return valores[j]
    return 0

print(obtener_elemento(1,0,[5, 4, 1, 2],[1, 2, 0, 1],[0, 2, 4, 4]))