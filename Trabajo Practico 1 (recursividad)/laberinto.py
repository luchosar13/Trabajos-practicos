matriz_Laberinto = [['#','','#','#','','','#'],
                    ['#','','','','#','','#'],
                    ['#','#','#','#','#','#',''],
                    ['#','','#','#','#','#','q']]


def laberinto(matriz, x, y, resultado = []):
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 'q'):
            verdad = True
            resultado.append([x,y])
            print('Has salido del laberinto con exito')
            print('La posición final del laberinto es: ', resultado)
        else:
            if(matriz[x][y] == '#'):
                matriz[x][y] = 'c'
                laberinto(matriz, x, y+1, resultado)
                laberinto(matriz, x, y-1, resultado)
                laberinto(matriz, x-1, y, resultado)
                laberinto(matriz, x+1, y, resultado)
                matriz[x][y] = 1


laberinto(matriz_Laberinto,0,0)


