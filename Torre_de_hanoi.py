from tkinter import Variable


hanoi = [['TORRE1', 'TORRE2', 'TORRE3'], ['MENOR', 'VACIO', 'VACIO'], ['MEDIO', 'VACIO', 'VACIO'], ['MAYOR', 'VACIO', 'VACIO']]

ubicacion_fichas = {'MENOR': [1,0], 'MEDIO': [2,0] , 'MAYOR': [3,0] } 

# ficha: [fila, columna]

for fila in range(4):
    for columna in range(3):
        print('{:<8}'.format(hanoi[fila][columna]), end= ' ')
    print()


# FUNCION MOVIMIENTO:


def movimiento(disco,torre_destino):
    for columna in range(3):
        if hanoi[0][columna] == torre_destino:
            for i in range(3,-1,-1):
                if hanoi[i][columna] == 'VACIO':
                    hanoi[i][columna] = disco

                    k = ubicacion_fichas[disco][0]
                    p = ubicacion_fichas[disco][1]
                    hanoi[k][p] = 'VACIO'

                    ubicacion_fichas[disco][0] = i
                    ubicacion_fichas[disco][1] = columna

                    break
                else:
                    continue
    for fila in range(4):
        for columna in range(3):
            print('{:<8}'.format(hanoi[fila][columna]), end= ' ')
        print()



while True:
    disco = input('Ingrese el disco que desea mover : ')
    torre_destino = input('Torre destino : ')
    movimiento(disco, torre_destino)
    