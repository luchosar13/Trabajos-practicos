vec = ['pistola','sable','armadura','sable de luz','rayo']

contador = [0]

def usarFuerza(vector,sableluz,contador):
    if (len(vector) == 1) and ((vector[0]) == sableluz) :
        print ('El sable de luz es el unico elemento de la mochila')
    else:
        if(vector[0] == sableluz):
            print ('El sable de luz fue encontrado')
        else:
            contador[0] += 1
            return usarFuerza(vector[1:],sableluz,contador)
                

usarFuerza(vec,'sable de luz', contador)
print('Para hallar el sable de luz hubo que sacar ',contador,' elementos de la mochila')



        
