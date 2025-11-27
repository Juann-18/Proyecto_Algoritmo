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


def obtener_fila_csr(i, num_columnas, valores, columnas, cfilas):
    fila = [0] * num_columnas
    for k in range(cfilas[i], cfilas[i+1]):
        col = columnas[k]
        fila[col] = valores[k]
    return fila

def obtener_fila_csc(i, num_columnas, valores, filas, ccolumnas):
    fila = [0] * num_columnas
    for j in range(num_columnas):
        for k in range(ccolumnas[j], ccolumnas[j+1]):
            if filas[k] == i:
                fila[j] = valores[k]
                break
    return fila


def obtener_fila_coo(i, num_columnas, valores, filas, columnas):
    fila = [0] * num_columnas
    for k in range(len(valores)):
        if filas[k] == i:
            fila[columnas[k]] = valores[k]
    return fila


def obtener_columna_coo(j, num_filas, valores, filas, columnas):
    columna = [0] * num_filas
    for k in range(len(valores)):
        if columnas[k] == j:
            columna[filas[k]] = valores[k]
    return columna


def obtener_columna_csr(j, num_filas, valores, columnas, cfilas):
    columna = [0] * num_filas
    for i in range(num_filas):
        for k in range(cfilas[i], cfilas[i+1]):
            if columnas[k] == j:
                columna[i] = valores[k]
                break
    return columna


def obtener_columna_csc(j, num_filas, valores, filas, ccolumnas):
    columna = [0] * num_filas
    for k in range(ccolumnas[j], ccolumnas[j+1]):
        fila_idx = filas[k]
        columna[fila_idx] = valores[k]
    return columna


def modificar_posicion_coo(i, j, nuevo_valor, valores, filas, columnas):

    valores = list(valores)
    filas = list(filas)
    columnas = list(columnas)
    
    # Buscar si el elemento ya existe
    encontrado = False
    indice = -1
    for k in range(len(valores)):
        if filas[k] == i and columnas[k] == j:
            encontrado = True
            indice = k
            break
    
    if encontrado:
        if nuevo_valor == 0:
            # Eliminar el elemento
            valores.pop(indice)
            filas.pop(indice)
            columnas.pop(indice)
        else:
            # Actualizar el valor
            valores[indice] = nuevo_valor
    else:
        # El elemento no existe
        if nuevo_valor != 0:
            # Agregar el nuevo elemento
            valores.append(nuevo_valor)
            filas.append(i)
            columnas.append(j)
    
    return valores, filas, columnas


def modificar_posicion_csr(i, j, nuevo_valor, valores, columnas, cfilas):
    valores = list(valores)
    columnas = list(columnas)
    cfilas = list(cfilas)
    
    # Buscar si el elemento ya existe en la fila i
    inicio_fila = cfilas[i]
    fin_fila = cfilas[i+1]
    encontrado = False
    posicion = -1
    
    for k in range(inicio_fila, fin_fila):
        if columnas[k] == j:
            encontrado = True
            posicion = k
            break
    
    if encontrado:
        if nuevo_valor == 0:
            # Eliminar el elemento
            valores.pop(posicion)
            columnas.pop(posicion)
            # Actualizar cfilas para todas las filas siguientes
            for fila_idx in range(i+1, len(cfilas)):
                cfilas[fila_idx] -= 1
        else:
            # Actualizar el valor
            valores[posicion] = nuevo_valor
    else:
        # El elemento no existe
        if nuevo_valor != 0:
            # Encontrar la posición correcta para insertar (ordenado por columna)
            posicion_insercion = inicio_fila
            for k in range(inicio_fila, fin_fila):
                if columnas[k] > j:
                    posicion_insercion = k
                    break
                posicion_insercion = k + 1
            
            # Insertar el nuevo elemento
            valores.insert(posicion_insercion, nuevo_valor)
            columnas.insert(posicion_insercion, j)
            # Actualizar cfilas para todas las filas siguientes
            for fila_idx in range(i+1, len(cfilas)):
                cfilas[fila_idx] += 1
    
    return valores, columnas, cfilas


def modificar_posicion_csc(i, j, nuevo_valor, valores, filas, ccolumnas):
    valores = list(valores)
    filas = list(filas)
    ccolumnas = list(ccolumnas)
    
    # Buscar si el elemento ya existe en la columna j
    inicio_col = ccolumnas[j]
    fin_col = ccolumnas[j+1]
    encontrado = False
    posicion = -1
    
    for k in range(inicio_col, fin_col):
        if filas[k] == i:
            encontrado = True
            posicion = k
            break
    
    if encontrado:
        if nuevo_valor == 0:
            # Eliminar el elemento
            valores.pop(posicion)
            filas.pop(posicion)
            # Actualizar ccolumnas para todas las columnas siguientes
            for col_idx in range(j+1, len(ccolumnas)):
                ccolumnas[col_idx] -= 1
        else:
            # Actualizar el valor
            valores[posicion] = nuevo_valor
    else:
        # El elemento no existe
        if nuevo_valor != 0:
            # Encontrar la posición correcta para insertar (ordenado por fila)
            posicion_insercion = inicio_col
            for k in range(inicio_col, fin_col):
                if filas[k] > i:
                    posicion_insercion = k
                    break
                posicion_insercion = k + 1
            
            # Insertar el nuevo elemento
            valores.insert(posicion_insercion, nuevo_valor)
            filas.insert(posicion_insercion, i)
            # Actualizar ccolumnas para todas las columnas siguientes
            for col_idx in range(j+1, len(ccolumnas)):
                ccolumnas[col_idx] += 1
    
    return valores, filas, ccolumnas


def sumar_matrices_coo(valores1, filas1, columnas1, valores2, filas2, columnas2):

    suma = {}
    
    # Agregar elementos de la primera matriz
    for k in range(len(valores1)):
        clave = (filas1[k], columnas1[k])
        suma[clave] = valores1[k]
    
    # Sumar elementos de la segunda matriz
    for k in range(len(valores2)):
        clave = (filas2[k], columnas2[k])
        if clave in suma:
            suma[clave] += valores2[k]
        else:
            suma[clave] = valores2[k]
    
    # Convertir el diccionario de vuelta a listas COO (eliminando ceros)
    valores_resultado = []
    filas_resultado = []
    columnas_resultado = []
    
    for (fila, col), valor in suma.items():
        if valor != 0:  # Solo agregar elementos no cero
            valores_resultado.append(valor)
            filas_resultado.append(fila)
            columnas_resultado.append(col)
    
    return valores_resultado, filas_resultado, columnas_resultado


def sumar_matrices_csr(valores1, columnas1, cfilas1, valores2, columnas2, cfilas2, num_filas, num_columnas):

    valores_resultado = []
    columnas_resultado = []
    cfilas_resultado = [0]
    
    # Iterar por cada fila
    for i in range(num_filas):
        # Crear un diccionario para esta fila: columna -> valor
        fila_suma = {}
        
        # Agregar elementos de la primera matriz en esta fila
        inicio1 = cfilas1[i]
        fin1 = cfilas1[i+1]
        for k in range(inicio1, fin1):
            fila_suma[columnas1[k]] = valores1[k]
        
        # Sumar elementos de la segunda matriz en esta fila
        inicio2 = cfilas2[i]
        fin2 = cfilas2[i+1]
        for k in range(inicio2, fin2):
            col = columnas2[k]
            if col in fila_suma:
                fila_suma[col] += valores2[k]
            else:
                fila_suma[col] = valores2[k]
        
        # Agregar elementos no cero a los resultados (ordenados por columna)
        columnas_ordenadas = sorted([col for col, val in fila_suma.items() if val != 0])
        for col in columnas_ordenadas:
            valores_resultado.append(fila_suma[col])
            columnas_resultado.append(col)
        
        cfilas_resultado.append(len(valores_resultado))
    
    return valores_resultado, columnas_resultado, cfilas_resultado


def sumar_matrices_csc(valores1, filas1, ccolumnas1, valores2, filas2, ccolumnas2, num_filas, num_columnas):

    valores_resultado = []
    filas_resultado = []
    ccolumnas_resultado = [0]
    
    # Iterar por cada columna
    for j in range(num_columnas):
        # Crear un diccionario para esta columna: fila -> valor
        columna_suma = {}
        
        # Agregar elementos de la primera matriz en esta columna
        inicio1 = ccolumnas1[j]
        fin1 = ccolumnas1[j+1]
        for k in range(inicio1, fin1):
            columna_suma[filas1[k]] = valores1[k]
        
        # Sumar elementos de la segunda matriz en esta columna
        inicio2 = ccolumnas2[j]
        fin2 = ccolumnas2[j+1]
        for k in range(inicio2, fin2):
            fila = filas2[k]
            if fila in columna_suma:
                columna_suma[fila] += valores2[k]
            else:
                columna_suma[fila] = valores2[k]
        
        # Agregar elementos no cero a los resultados (ordenados por fila)
        filas_ordenadas = sorted([fila for fila, val in columna_suma.items() if val != 0])
        for fila in filas_ordenadas:
            valores_resultado.append(columna_suma[fila])
            filas_resultado.append(fila)
        
        ccolumnas_resultado.append(len(valores_resultado))
    
    return valores_resultado, filas_resultado, ccolumnas_resultado


def transpuesta_coo(valores, filas, columnas, num_filas_original, num_columnas_original):

    # En COO, la transpuesta es simplemente intercambiar filas y columnas
    # Pero necesitamos mantener el orden correcto
    # Ordenamos por (columna, fila) para mantener consistencia
    elementos = list(zip(valores, filas, columnas))
    # Ordenar por columna (nueva fila) y luego por fila (nueva columna)
    elementos_ordenados = sorted(elementos, key=lambda x: (x[2], x[1]))
    
    valores_transp = [elem[0] for elem in elementos_ordenados]
    filas_transp = [elem[2] for elem in elementos_ordenados]  # columnas originales -> filas nuevas
    columnas_transp = [elem[1] for elem in elementos_ordenados]  # filas originales -> columnas nuevas
    
    return valores_transp, filas_transp, columnas_transp


def transpuesta_csr(valores, columnas, cfilas, num_filas_original, num_columnas_original):

    # La transpuesta de CSR es CSC
    # Recolectar todos los elementos con sus nuevas coordenadas
    elementos = []
    
    for i in range(num_filas_original):
        inicio = cfilas[i]
        fin = cfilas[i+1]
        for k in range(inicio, fin):
            col_orig = columnas[k]
            valor = valores[k]
            # En la transpuesta: fila original i -> columna nueva i
            #                   columna original col_orig -> fila nueva col_orig
            elementos.append((valor, col_orig, i))  # (valor, nueva_fila, nueva_columna)
    
    # Ordenar por nueva fila (col_orig) y luego por nueva columna (i)
    elementos.sort(key=lambda x: (x[1], x[2]))
    
    # Construir CSC
    valores_transp = []
    filas_transp = []
    ccolumnas_transp = [0]
    
    columna_actual = -1
    for valor, nueva_fila, nueva_col in elementos:
        # Si cambiamos de columna, actualizar ccolumnas
        while nueva_col > columna_actual:
            columna_actual += 1
            ccolumnas_transp.append(len(valores_transp))
        
        valores_transp.append(valor)
        filas_transp.append(nueva_fila)
    
    # Completar ccolumnas para las columnas vacías al final
    while columna_actual < num_columnas_original - 1:
        columna_actual += 1
        ccolumnas_transp.append(len(valores_transp))
    
    return valores_transp, filas_transp, ccolumnas_transp


def transpuesta_csc(valores, filas, ccolumnas, num_filas_original, num_columnas_original):
    
    # La transpuesta de CSC es CSR
    # Recolectar todos los elementos con sus nuevas coordenadas
    elementos = []
    
    for j in range(num_columnas_original):
        inicio = ccolumnas[j]
        fin = ccolumnas[j+1]
        for k in range(inicio, fin):
            fil_orig = filas[k]
            valor = valores[k]
            # En la transpuesta: columna original j -> fila nueva j
            #                   fila original fil_orig -> columna nueva fil_orig
            elementos.append((valor, j, fil_orig))  # (valor, nueva_fila, nueva_columna)
    
    # Ordenar por nueva fila (j) y luego por nueva columna (fil_orig)
    elementos.sort(key=lambda x: (x[1], x[2]))
    
    # Construir CSR
    valores_transp = []
    columnas_transp = []
    cfilas_transp = [0]
    
    fila_actual = -1
    for valor, nueva_fila, nueva_col in elementos:
        # Si cambiamos de fila, actualizar cfilas
        while nueva_fila > fila_actual:
            fila_actual += 1
            cfilas_transp.append(len(valores_transp))
        
        valores_transp.append(valor)
        columnas_transp.append(nueva_col)
    
    # Completar cfilas para las filas vacías al final
    while fila_actual < num_filas_original - 1:
        fila_actual += 1
        cfilas_transp.append(len(valores_transp))
    
    return valores_transp, columnas_transp, cfilas_transp

# print(obtener_elemento(1,1,[ 2,4,8,9,1,3,5,6,1,2,4,7,1,1], [1,6,1,2,5,3,0,5,0,1,0,2,5], [0,2,5,6,6,8,10,11,13]
# ))
