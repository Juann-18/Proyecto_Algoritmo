from CSC import matriz_a_csc
from CSR import matriz_a_csr
from COO import matriz_a_coo
from Operaciones import (
    obtener_elemento_csr, obtener_elemento_coo, obtener_elemento_csc,
    obtener_fila_csr, obtener_fila_coo, obtener_fila_csc,
    obtener_columna_csr, obtener_columna_coo, obtener_columna_csc,
    modificar_posicion_csr, modificar_posicion_coo, modificar_posicion_csc,
    sumar_matrices_csr, sumar_matrices_coo, sumar_matrices_csc,
    transpuesta_csr, transpuesta_coo, transpuesta_csc
)



def menu(): 
    matriz = []
    if not matriz: 
        matriz = agregar_matriz()
        mostrar_matriz(matriz)
    while(True):
        print("")
        print("MENÚ PRINCIPAL")
        print("1. Obtener la representación")
        print("2. Operaciones")
        print("3. Suma de matrices")
        print("4. Matriz transpuesta")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese la opción: "))
            
            if opcion == 1: 
                submenu(matriz)
            elif opcion == 2:
                submenu_operaciones(matriz)
            elif opcion == 3:
                submenu_suma_matrices()
            elif opcion == 4:
                submenu_transpuesta()
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, ingrese 1, 2, 3, 4 o 5.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        except Exception as e:
            print(f"Error inesperado: {e}")

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
    try:
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        
        if filas <= 0 or columnas <= 0:
            print("Error: Las dimensiones deben ser mayores a 0.")
            return agregar_matriz()
        
        print(f"\nIngrese los valores de la matriz ({filas}x{columnas}):")
        for i in range(filas):
            fila = []
            for j in range(columnas):
                n = int(input(f"  Fila {i+1}, Columna {j+1}: "))
                fila.append(n)
            matriz.append(fila)
        return matriz
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return agregar_matriz()


def mostrar_matriz(matriz):
    print("\nMatriz:")
    for i in range(len(matriz)):
        print(f"  {matriz[i]}")

def submenu(matriz):
    mostrar_matriz(matriz)
    print("\nREPRESENTACIONES DE MATRIZ DISPERSA")
    
    # COO
    val, fil, col = matriz_a_coo(matriz)
    print("\n1. COO")
    print("   Valores:  ", val)
    print("   Filas:    ", fil)
    print("   Columnas: ", col)

    # CSR
    val, columnas, cfilas = matriz_a_csr(matriz)
    print("\n2. CSR")
    print("   Valores:  ", val)
    print("   Columnas: ", columnas)
    print("   CFilas:   ", cfilas)
    
    # CSC
    val, filas, ccolumnas = matriz_a_csc(matriz)
    print("\n3. CSC")
    print("   Valores:   ", val)
    print("   Filas:     ", filas)
    print("   CColumnas: ", ccolumnas)

def submenu_operaciones(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if matriz else 0
    
    while True:
        print("")
        print("OPERACIONES")
        print("1. Obtener elemento")
        print("2. Obtener fila")
        print("3. Obtener columna")
        print("4. Modificar posición")
        print("5. Volver al menú principal")
        
        try:
            opcion = int(input("Ingrese la opción: "))
            
            if opcion == 1:
                submenu_obtener_elemento(matriz, filas, columnas)
            elif opcion == 2:
                submenu_obtener_fila(matriz, filas, columnas)
            elif opcion == 3:
                submenu_obtener_columna(matriz, filas, columnas)
            elif opcion == 4:
                submenu_modificar_posicion(matriz, filas, columnas)
            elif opcion == 5:
                break
            else:
                print("Opción inválida. Por favor, ingrese 1, 2, 3, 4 o 5.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        except Exception as e:
            print(f"Error inesperado: {e}")


def submenu_obtener_elemento(matriz, num_filas, num_columnas):
    try:
        print("OBTENER ELEMENTO")
        i = int(input("Ingrese el índice de la fila (i): "))
        j = int(input("Ingrese el índice de la columna (j): "))
        
        if i < 0 or i >= num_filas or j < 0 or j >= num_columnas:
            print(f"Error: Los índices deben estar en el rango [0, {num_filas-1}] para filas y [0, {num_columnas-1}] para columnas.")
            return
        
        print("\nSeleccione el formato:")
        print("1. COO")
        print("2. CSR")
        print("3. CSC")
        
        formato = int(input("Ingrese la opción: "))
        
        mostrar_matriz(matriz)
        print("")
        
        if formato == 1:
            val, fil, col = matriz_a_coo(matriz)
            resultado = obtener_elemento_coo(i, j, val, fil, col)
            print(f"El elemento en la posición ({i},{j}) es: {resultado} [COO]")
        elif formato == 2:
            val, columnas, cfilas = matriz_a_csr(matriz)
            resultado = obtener_elemento_csr(i, j, val, columnas, cfilas)
            print(f"El elemento en la posición ({i},{j}) es: {resultado} [CSR]")
        elif formato == 3:
            val, filas, ccolumnas = matriz_a_csc(matriz)
            resultado = obtener_elemento_csc(i, j, val, filas, ccolumnas)
            print(f"El elemento en la posición ({i},{j}) es: {resultado} [CSC]")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def submenu_obtener_fila(matriz, num_filas, num_columnas):
    try:
        print("OBTENER FILA")
        i = int(input(f"Ingrese el índice de la fila (0 a {num_filas-1}): "))
        
        if i < 0 or i >= num_filas:
            print(f"Error: El índice de fila debe estar en el rango [0, {num_filas-1}].")
            return
        
        print("\nSeleccione el formato:")
        print("1. COO")
        print("2. CSR")
        print("3. CSC")
        
        formato = int(input("Ingrese la opción: "))
        
        mostrar_matriz(matriz)
        print("")
        
        if formato == 1:
            val, fil, col = matriz_a_coo(matriz)
            resultado = obtener_fila_coo(i, num_columnas, val, fil, col)
            print(f"Fila {i}: {resultado} [COO]")
        elif formato == 2:
            val, columnas, cfilas = matriz_a_csr(matriz)
            resultado = obtener_fila_csr(i, num_columnas, val, columnas, cfilas)
            print(f"Fila {i}: {resultado} [CSR]")
        elif formato == 3:
            val, filas, ccolumnas = matriz_a_csc(matriz)
            resultado = obtener_fila_csc(i, num_columnas, val, filas, ccolumnas)
            print(f"Fila {i}: {resultado} [CSC]")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def submenu_obtener_columna(matriz, num_filas, num_columnas):
    try:
        print("OBTENER COLUMNA")
        j = int(input(f"Ingrese el índice de la columna (0 a {num_columnas-1}): "))
        
        if j < 0 or j >= num_columnas:
            print(f"Error: El índice de columna debe estar en el rango [0, {num_columnas-1}].")
            return
        
        print("\nSeleccione el formato:")
        print("1. COO")
        print("2. CSR")
        print("3. CSC")
        
        formato = int(input("Ingrese la opción: "))
        
        mostrar_matriz(matriz)
        print("")
        
        if formato == 1:
            val, fil, col = matriz_a_coo(matriz)
            resultado = obtener_columna_coo(j, num_filas, val, fil, col)
            print(f"Columna {j}: {resultado} [COO]")
        elif formato == 2:
            val, columnas, cfilas = matriz_a_csr(matriz)
            resultado = obtener_columna_csr(j, num_filas, val, columnas, cfilas)
            print(f"Columna {j}: {resultado} [CSR]")
        elif formato == 3:
            val, filas, ccolumnas = matriz_a_csc(matriz)
            resultado = obtener_columna_csc(j, num_filas, val, filas, ccolumnas)
            print(f"Columna {j}: {resultado} [CSC]")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def submenu_modificar_posicion(matriz, num_filas, num_columnas):
    try:
        print("MODIFICAR POSICIÓN")
        i = int(input("Ingrese el índice de la fila (i): "))
        j = int(input("Ingrese el índice de la columna (j): "))
        
        if i < 0 or i >= num_filas or j < 0 or j >= num_columnas:
            print(f"Error: Los índices deben estar en el rango [0, {num_filas-1}] para filas y [0, {num_columnas-1}] para columnas.")
            return
        
        nuevo_valor = int(input("Ingrese el nuevo valor: "))
        
        print("\nSeleccione el formato:")
        print("1. COO")
        print("2. CSR")
        print("3. CSC")
        
        formato = int(input("Ingrese la opción: "))
        
        mostrar_matriz(matriz)
        print("")
        
        if formato == 1:
            val, fil, col = matriz_a_coo(matriz)
            print("Representación COO ANTES de modificar:")
            print(f"   Valores:  {val}")
            print(f"   Filas:    {fil}")
            print(f"   Columnas: {col}")
            
            val_mod, fil_mod, col_mod = modificar_posicion_coo(i, j, nuevo_valor, val, fil, col)
            
            print("\nRepresentación COO DESPUÉS de modificar:")
            print(f"   Valores:  {val_mod}")
            print(f"   Filas:    {fil_mod}")
            print(f"   Columnas: {col_mod}")
            print(f"\n✓ Posición ({i},{j}) modificada a {nuevo_valor} [COO]")
            
        elif formato == 2:
            val, columnas, cfilas = matriz_a_csr(matriz)
            print("Representación CSR ANTES de modificar:")
            print(f"   Valores:  {val}")
            print(f"   Columnas: {columnas}")
            print(f"   CFilas:   {cfilas}")
            
            val_mod, columnas_mod, cfilas_mod = modificar_posicion_csr(i, j, nuevo_valor, val, columnas, cfilas)
            
            print("\nRepresentación CSR DESPUÉS de modificar:")
            print(f"   Valores:  {val_mod}")
            print(f"   Columnas: {columnas_mod}")
            print(f"   CFilas:   {cfilas_mod}")
            print(f"\n✓ Posición ({i},{j}) modificada a {nuevo_valor} [CSR]")
            
        elif formato == 3:
            val, filas, ccolumnas = matriz_a_csc(matriz)
            print("Representación CSC ANTES de modificar:")
            print(f"   Valores:   {val}")
            print(f"   Filas:     {filas}")
            print(f"   CColumnas: {ccolumnas}")
            
            val_mod, filas_mod, ccolumnas_mod = modificar_posicion_csc(i, j, nuevo_valor, val, filas, ccolumnas)
            
            print("\nRepresentación CSC DESPUÉS de modificar:")
            print(f"   Valores:   {val_mod}")
            print(f"   Filas:     {filas_mod}")
            print(f"   CColumnas: {ccolumnas_mod}")
            print(f"\n✓ Posición ({i},{j}) modificada a {nuevo_valor} [CSC]")
            
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def submenu_suma_matrices():
    try:
        print("SUMA DE MATRICES")
        
        print("\nSeleccione el formato:")
        print("1. COO")
        print("2. CSR")
        print("3. CSC")
        
        formato = int(input("Ingrese la opción: "))
        
        if formato not in [1, 2, 3]:
            print("Opción inválida.")
            return
        
        # Solicitar primera matriz
        print("PRIMERA MATRIZ")
        matriz1 = agregar_matriz()
        mostrar_matriz(matriz1)
        
        # Solicitar segunda matriz
        print("SEGUNDA MATRIZ")
        matriz2 = agregar_matriz()
        mostrar_matriz(matriz2)
        
        # Verificar que las matrices tengan las mismas dimensiones
        if len(matriz1) != len(matriz2) or (matriz1 and len(matriz1[0]) != len(matriz2[0])):
            print("\nError: Las matrices deben tener las mismas dimensiones para poder sumarse.")
            return
        
        num_filas = len(matriz1)
        num_columnas = len(matriz1[0]) if matriz1 else 0
        
        print("RESULTADO DE LA SUMA")
        
        if formato == 1:
            # COO
            val1, fil1, col1 = matriz_a_coo(matriz1)

            print(val1, fil1, col1 )
            val2, fil2, col2 = matriz_a_coo(matriz2)
            print(val2, fil2, col2)
            
            print("\nPrimera matriz (COO):")
            print(f"   Valores:  {val1}")
            print(f"   Filas:    {fil1}")
            print(f"   Columnas: {col1}")
            
            print("\nSegunda matriz (COO):")
            print(f"   Valores:  {val2}")
            print(f"   Filas:    {fil2}")
            print(f"   Columnas: {col2}")
            
            val_res, fil_res, col_res = sumar_matrices_coo(val1, fil1, col1, val2, fil2, col2)
            
            print("\nResultado de la suma (COO):")
            print(f"   Valores:  {val_res}")
            print(f"   Filas:    {fil_res}")
            print(f"   Columnas: {col_res}")
            
        elif formato == 2:
            # CSR
            val1, col1, cfil1 = matriz_a_csr(matriz1)
            val2, col2, cfil2 = matriz_a_csr(matriz2)
            
            print("\nPrimera matriz (CSR):")
            print(f"   Valores:  {val1}")
            print(f"   Columnas: {col1}")
            print(f"   CFilas:   {cfil1}")
            
            print("\nSegunda matriz (CSR):")
            print(f"   Valores:  {val2}")
            print(f"   Columnas: {col2}")
            print(f"   CFilas:   {cfil2}")
            
            val_res, col_res, cfil_res = sumar_matrices_csr(
                val1, col1, cfil1, val2, col2, cfil2, num_filas, num_columnas
            )
            
            print("\nResultado de la suma (CSR):")
            print(f"   Valores:  {val_res}")
            print(f"   Columnas: {col_res}")
            print(f"   CFilas:   {cfil_res}")
            
        elif formato == 3:
            # CSC
            val1, fil1, ccol1 = matriz_a_csc(matriz1)
            val2, fil2, ccol2 = matriz_a_csc(matriz2)
            
            print("\nPrimera matriz (CSC):")
            print(f"   Valores:   {val1}")
            print(f"   Filas:     {fil1}")
            print(f"   CColumnas: {ccol1}")
            
            print("\nSegunda matriz (CSC):")
            print(f"   Valores:   {val2}")
            print(f"   Filas:     {fil2}")
            print(f"   CColumnas: {ccol2}")
            
            val_res, fil_res, ccol_res = sumar_matrices_csc(
                val1, fil1, ccol1, val2, fil2, ccol2, num_filas, num_columnas
            )
            
            print("\nResultado de la suma (CSC):")
            print(f"   Valores:   {val_res}")
            print(f"   Filas:     {fil_res}")
            print(f"   CColumnas: {ccol_res}")
        
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def submenu_transpuesta():
    try:
        print("MATRIZ TRANSPUESTA")
        
        # Solicitar matriz
        matriz = agregar_matriz()
        mostrar_matriz(matriz)
        
        num_filas = len(matriz)
        num_columnas = len(matriz[0]) if matriz else 0
        
        print("\nSeleccione el formato:")
        print("1. COO")
        print("2. CSR")
        print("3. CSC")
        
        formato = int(input("Ingrese la opción: "))
        
        if formato not in [1, 2, 3]:
            print("Opción inválida.")
            return
        
        print("RESULTADO DE LA TRANSPUESTA")
        
        if formato == 1:
            # COO
            val, fil, col = matriz_a_coo(matriz)
            
            print("\nMatriz original (COO):")
            print(f"   Valores:  {val}")
            print(f"   Filas:    {fil}")
            print(f"   Columnas: {col}")
            
            val_transp, fil_transp, col_transp = transpuesta_coo(
                val, fil, col, num_filas, num_columnas
            )
            
            print("\nMatriz transpuesta (COO):")
            print(f"   Valores:  {val_transp}")
            print(f"   Filas:    {fil_transp}")
            print(f"   Columnas: {col_transp}")
            print(f"\n✓ Dimensiones: {num_filas}x{num_columnas} -> {num_columnas}x{num_filas}")
            
        elif formato == 2:
            # CSR -> CSC (transpuesta)
            val, columnas, cfilas = matriz_a_csr(matriz)
            
            print("\nMatriz original (CSR):")
            print(f"   Valores:  {val}")
            print(f"   Columnas: {columnas}")
            print(f"   CFilas:   {cfilas}")
            
            val_transp, filas_transp, ccolumnas_transp = transpuesta_csr(
                val, columnas, cfilas, num_filas, num_columnas
            )
            
            print("\nMatriz transpuesta (CSC):")
            print(f"   Valores:   {val_transp}")
            print(f"   Filas:     {filas_transp}")
            print(f"   CColumnas: {ccolumnas_transp}")
            print(f"\n✓ Dimensiones: {num_filas}x{num_columnas} -> {num_columnas}x{num_filas}")
            print("  (CSR transpuesta = CSC)")
            
        elif formato == 3:
            # CSC -> CSR (transpuesta)
            val, filas, ccolumnas = matriz_a_csc(matriz)
            
            print("\nMatriz original (CSC):")
            print(f"   Valores:   {val}")
            print(f"   Filas:     {filas}")
            print(f"   CColumnas: {ccolumnas}")
            
            val_transp, columnas_transp, cfilas_transp = transpuesta_csc(
                val, filas, ccolumnas, num_filas, num_columnas
            )
            
            print("\nMatriz transpuesta (CSR):")
            print(f"   Valores:  {val_transp}")
            print(f"   Columnas: {columnas_transp}")
            print(f"   CFilas:   {cfilas_transp}")
            print(f"\n✓ Dimensiones: {num_filas}x{num_columnas} -> {num_columnas}x{num_filas}")
            print("  (CSC transpuesta = CSR)")
        
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


menu()
