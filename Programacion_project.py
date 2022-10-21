
A = [["TORRE 1" , "TORRE 2", "TORRE 3"],["MENOR", "VACIO", "VACIO"], ["MEDIO", "VACIO", "VACIO"],["MAYOR", "VACIO", "VACIO"]]
M = 4  # filas
N = 3  # columnas
print("Impresión de la matriz:")
print("__________________")
for i in range(M):
    for j in range(N):
        print('{:^10}'.format(A[i][j]), end=" ")
    print("")
while True:
    contador = 1
    mover = input("Ingrese el disco que de sea mover :")
    destino = input("Ingrese la torre de destino: ")
    ultima_jugada = 1
    if contador <= ultima_jugada:
        for i in range(M):
            for j in range(N):
                if A[i][j] == mover:
                    A[i][j] = "VACIO"
                if destino == A[0][j]:
                    A[3][j] = mover
                print('{:^10}'.format(A[i][j]), end=" ")
            print("")
    elif contador >= ultima_jugada:
        break
    contador += 1

