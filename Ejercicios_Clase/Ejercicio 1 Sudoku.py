# 🔹 Ejercicios Propuestos (Nivel Avanzado)
# 1. Sudoku simplificado (4x4)

# Generar un tablero 4x4 con números del 1 al 4 (pueden estar repetidos).

# Escribir una función que valide si una fila tiene todos los números distintos.

# Escribir otra que valide una columna.

# (Extra) Validar que cada subcuadro 2x2 también cumpla la condición.
# 👉 Aplican listas anidadas, bucles y slicing.

base=list(range(1,5))
sudoku_tabla = []
bandera = False

for i in range(4):
    fila = base[i:] + base[:i]
    sudoku_tabla.append(fila)

for fila in sudoku_tabla:
    print(fila)

for fila in sudoku_tabla:
    if fila[i: ] != fila[:i]:
        bandera = True
    else:
        bandera = False

if bandera == True:
    print("Las filas tienen numeros distintos")
else:
    print("Las filas contienen algunos numeros repetidos")

