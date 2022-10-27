hanoi = [['TORRE1', 'TORRE2', 'TORRE3'], ['MENOR', 'VACIO', 'VACIO'], ['MEDIO', 'VACIO', 'VACIO'], ['MAYOR', 'VACIO', 'VACIO']]

ubicacion_fichas = {'MENOR': [1,0], 'MEDIO': [2,0] , 'MAYOR': [3,0] } 

# ficha: [fila, columna]

for fila in range(4):
    for columna in range(3):
        print('{:<8}'.format(hanoi[fila][columna]), end= ' ')
    print()


# FUNCION MOVIMIENTO (FUNCIONA) #############################################################################


disco = input('Ingrese el disco que desea mover : ')
torre_destino = input('Torre destino : ')

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


disco = input('Ingrese el disco que desea mover : ')
torre_destino = input('Torre destino : ')

for fila in range(len(hanoi)):
    for columna in range(3):
            if hanoi[fila][columna] == torre_destino:
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

print(ubicacion_fichas.items())


#############################################################################################



#FUNCION VALIDACION DEL MOVIMIENTO DE LA FICHA (FUNCIONA) #################################################

def validacion_movimiento(disco, i , columna):
    if i != 3:
        if disco == 'MENOR':
            if hanoi[i + 1][columna] == 'MEDIO' or hanoi[i + 1][columna] == 'MAYOR':
                validacion_move = True
            else:
                validacion_move = False
        elif disco == 'MEDIO':
            if hanoi[i + 1][columna] == 'MAYOR':
                validacion_move = True
            else:
                validacion_move = False
        else:
            if hanoi[i +  1][columna] != 'MENOR' or hanoi[i + 1][columna] != 'MEDIO' :
                validacion_move = True
            else: False
    else:
        validacion_move = True
    return validacion_move

print(validacion_movimiento('MEDIO', 2, 1))

###########################################################################################



#FUNCION VALIDACION DEL LLAMADO DEL DISCO (FUNCIONA) #############################################
def validacion_llamado_disco(matriz, dict, disco):
    if matriz[dict[disco][0] - 1][dict[disco][1]] != 'VACIO':
        validacion_disco = False
    else:
        if matriz[dict[disco][0] - 1][dict[disco][1]] in matriz[0]:
            validacion_disco = True
    return validacion_disco


print('2')
print(hanoi)
print(ubicacion_fichas)
print(validacion_llamado_disco(hanoi,ubicacion_fichas, 'MENOR'))

##############################################################################################



#FUNCION VALIDACION DE LA TORRE (FUNCIONA) ###########################################################3

def validacion_torre(matriz):
    cont_val = 0
    for columna in range(1,3):
        for fila in range(1,4):
            if fila == 1 and matriz[fila][columna] == 'MENOR':
                cont_val+=1
            elif fila == 2 and matriz[fila][columna] == 'MEDIO':
                cont_val+=1
            elif fila == 3 and matriz[fila][columna] == 'MAYOR':
                cont_val+=1
            else:
                continue
    return cont_val
